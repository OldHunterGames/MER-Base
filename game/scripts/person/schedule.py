# -*- coding: UTF-8 -*-
from collections import OrderedDict, defaultdict
from copy import copy

import mer_utilities as utilities
from mer_command import MenuCard

import renpy.exports as renpy
import renpy.store as store


class ExternController(object):

    def __init__(self, available_callable, blocker_callable, release_callable, all_callable):
        self._available = available_callable
        self._blocker = blocker_callable
        self._release = release_callable
        self._all = all_callable

    def get(self):
        return self._available()

    def use(self, schedule_obj):
        self._blocker(schedule_obj)

    def release(self, schedule_obj):
        self._release(schedule_obj)

    def all(self):
        return self._all()


class ScheduleObject(object):

    def __init__(self, id, data_dict, locked=False, *args, **kwargs):
        self._data = data_dict[id]
        self.id = id
        self.locked = locked

    def _image_raw(self):
        img = self.get_image()
        if img is None:
            return utilities.empty_card()
        return img

    def image(self, size=None):
        if size is None:
            size = (200, 300)
        return renpy.display.im.Scale(self._image_raw(), *size)

    @property
    def _image(self):
        return self._data.get('image')

    def get_image(self):
        # testing image getting system
        path = 'images/%s/%s' % (self._image, self.id)
        images = utilities.get_files(path)
        try:
            img = images[0]
        except IndexError:
            img = None
        return img

    @property
    def cost(self):
        try:
            cost = self._data['cost']
        except KeyError:
            cost = 0
        return cost

    def __getattr__(self, key):
        try:
            value = self.__dict__['_data'][key]
        except KeyError:
            raise AttributeError(key)
        return value

    def description(self):
        return self._data.get('description', 'No description')

    def name(self):
        return self._data.get('name', 'No name')

    def use(self, person, type):
        self._on_use(person)
        lbl = str(self.world).lower() + '_%s' % type + '_%s' % self.id
        if renpy.has_label(lbl):
            renpy.call_in_new_context(lbl, person)
        self.locked = False

    def lock(self):
        self.locked = True

    def _on_use(self, person):
        return


class ScheduleJob(ScheduleObject):

    def __init__(self, *args, **kwargs):
        super(ScheduleJob, self).__init__(*args, **kwargs)
        self.productivity = 1

    def full_description(self):
        string = self.name()
        string += '\n current effort: %s' % utilities.encolor_text(
            store.focus_description[self.focus], self.focus)
        if self.focus != 5:
            string += '\n needed effort: %s' %\
                store.effort_quality[self.focus + 1]
        return string

    def _on_use(self, person):
        if self.attribute is not None:
            if person.player_controlled:
                renpy.call_in_new_context(
                    'lbl_jobcheck', self, person)


class Schedule(object):
    JOB = 'job'
    RATION = 'ration'
    ACCOMMODATION = 'accommodation'
    EXTRA = 'extra'

    def __init__(self):

        self._available_external = defaultdict(list)

        self._available = {
            self.RATION: [],
            self.JOB: [],
            self.ACCOMMODATION: [],
            self.EXTRA: []
        }

        self._current = {
            self.RATION: None,
            self.JOB: None,
            self.ACCOMMODATION: None,
            self.EXTRA: OrderedDict({0: None, 1: None, 2: None})
        }

        self._defaults = {
            self.JOB: None,
            self.RATION: None,
            self.ACCOMMODATION: None
        }

    def add_available(self, slot, obj):
        self._available[slot].append(obj)

    def extern_available(self, slot, extern_controller):
        self._available_external[slot].append(extern_controller)

    def unextern_available(self, slot, extern_controller):
        self._available_external[slot].remove(extern_controller)
        for key, value in self._current.items():
            extern_schedule = extern_controller.all()
            if value in extern_schedule:
                self.set_current(key, None)

    def _get_available_extras(self, world):
        available = self._get_available(self.EXTRA)
        return [
            i for i in available if
            i.world == world and i not in self._current[self.EXTRA].values()]

    def _get_available(self, slot):
        available = list()
        for i in self._available_external[slot]:
            available.extend(i.get())
        available.extend(self._available[slot])
        return available

    def get_available(self, slot, world):
        if slot == self.EXTRA:
            return self._get_available_extras(world)
        available = self._get_available(slot)
        if self._defaults[slot] != self.get_current(slot):
            available.append(self._defaults[slot])
        return [i for i in available if i.world == world]

    def _remove_available_extra(self, obj):
        for key, value in self._current[self.EXTRA].items():
            if value == obj:
                self._current[self.EXTRA][key] = None
                return

    def remove_available(self, slot, obj):
        if slot == self.EXTRA:
            self._remove_available_extra(obj)
        if self.get_current(slot) == obj:
            self._current[slot] = None
        self._available[slot].remove(obj)

    def set_default(self, slot, obj):
        self._defaults[slot] = obj

    def use(self, person):
        for key, value in self._current.items():
            if key == self.EXTRA:
                for i in value.values():
                    if i is not None:
                        i.use(person, self.EXTRA)
            else:
                self.get_current(key).use(person, key)

    def _extras_cost(self):
        return sum([i.cost for i in self._current[self.EXTRA].values() if i is not None])

    def get_cost(self):
        return sum(
            [i.cost for i in self._current.values() if
                isinstance(i, ScheduleObject)]) + \
            self._extras_cost()

    def get_current(self, slot):
        if self._current[slot] is None:
            return self._defaults[slot]
        return self._current[slot]

    def set_current(self, slot, obj):
        for i in self._available_external[slot]:
            extern = i.all()
            if obj in extern:
                i.use(obj)
            if self._current[slot] in extern:
                i.release(self._current[slot])
        self._current[slot] = obj

    def set_extra(self, index, obj):
        for i in self._available_external[self.EXTRA]:
            extern = i.all()
            if obj in extern:
                i.use(obj)
            if self._current[self.EXTRA][index] in extern:
                i.release(self._current[self.EXTRA][index])
        self._current[self.EXTRA][index] = obj

    def get_extra(self, index):
        return self._current[self.EXTRA][index]
