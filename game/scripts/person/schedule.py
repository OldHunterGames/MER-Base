# -*- coding: UTF-8 -*-
from collections import OrderedDict, defaultdict
from copy import copy

import mer_utilities as utilities
from mer_command import MenuCard

import renpy.exports as renpy
import renpy.store as store


class ScheduleObject(object):

    def __init__(self, id, data_dict, locked=False, *args, **kwargs):
        self._data = data_dict[id]
        self.id = id
        self.locked = locked
        self.active = False

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

    def slot(self):
        return self._data['slot']

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

    def resource(self):
        return self._data.get('resources', {})


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

    def used_resources(self):
        resources = defaultdict(int)
        for key in self._current.keys():
            if key != self.EXTRA:
                resource = self.get_current(key).resource()
                for key, value in resource.items():
                    resources[key] += value
            else:
                for i in range(0, 3):
                    value = self.get_extra(i)
                    if value is not None:
                        resource = value.resource()
                        for key, value in resource.items():
                            resources[key] += value
        return resources

    def add_available(self, obj):
        self._available[obj.slot()].append(obj)

    def _get_available(self, slot):
        return [i for i in self._available[slot] if not i.active]

    def get_available(self, slot, world):
        available = self._get_available(slot)
        if slot != self.EXTRA:
            if self._defaults[slot] != self.get_current(slot):
                available.append(self._defaults[slot])
        return [i for i in available if i.world == world]

    def _remove_available_extra(self, obj):
        for key, value in self._current[self.EXTRA].items():
            if value == obj:
                self._current[self.EXTRA][key] = None
                return

    def remove_available(self, obj):
        slot = obj.slot()
        if slot == self.EXTRA:
            self._remove_available_extra(obj)
        if self.get_current(slot) == obj:
            self._current[slot] = None
        self._available[slot].remove(obj)

    def set_default(self, obj):
        self._defaults[obj.slot()] = obj

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
            [self.get_current(key).cost for key in self._current.keys() if
                key != self.EXTRA]) + \
            self._extras_cost()

    def get_current(self, slot):
        if self._current[slot] is None:
            return self._defaults[slot]
        return self._current[slot]

    def set_current(self, obj):
        if self._current[obj.slot()] is not None:
            self._current[obj.slot()].active = False
        obj.active = True
        self._current[obj.slot()] = obj

    def set_extra(self, index, obj):
        if self._current[self.EXTRA][index] is not None:
            self._current[self.EXTRA][index].active = False
        obj.active = True
        self._current[self.EXTRA][index] = obj

    def get_extra(self, index):
        return self._current[self.EXTRA][index]
