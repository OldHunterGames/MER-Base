# -*- coding: <UTF-8> -*-
__author__ = 'OldHuntsman'
from random import *
import renpy.store as store
import renpy.exports as renpy

from modifiers import Modifiable
import mer_utilities


class Feature(Modifiable):

    def __init__(self, id_, data_dict='person_features', time=None,
                 *args, **kwargs):
        try:
            data_dict = getattr(store, data_dict)
            stats = data_dict[id_]
        except KeyError:
            raise KeyError("no feature named %s in %s" % (id_, data_dict))
        self.init_modifiable()
        self.id = id_
        self.stats = stats
        self._time = time
        self._revealed = False   # true if the feature is revealed to player

    def count_modifiers(self, attr):
        mods = self.stats.get('modifiers', 0)
        if mods == 0:
            return mods
        return mods.get(attr, 0)

    def get_nicknames(self):
        return self.stats.get('nicknames', list())

    def has_tag(self, tag):
        return tag in self.tags

    def __getattr__(self, key):
        try:
            value = self.__dict__['stats'][key]
        except KeyError:
            raise AttributeError(key)
        else:
            return value

    def _image(self):
        return self.stats['image']

    def get_image(self):
        # testing image getting system
        path = 'images/%s/%s' % (self._image(), self._id)
        images = mer_utilities.get_files(path)
        try:
            img = images[0]
        except IndexError:
            img = None
        return img

    def image(self):
        img = self.get_image()
        if img is None:
            return empty_card()
        return img

    def description(self):
        return self.stats.get('description', 'No description')

    def name(self):
        return self.stats['name']

    def set_time(self, time):
        self._time = time

    @property
    def slot(self):
        try:
            slot = self.stats['slot']
        except KeyError:
            slot = None
        return slot

    @property
    def modifiers(self):
        try:
            return self.stats['modifiers']
        except KeyError:
            return dict()

    @property
    def visible(self):
        return self.stats['visible']

    @property
    def time(self):
        return self._time

    @property
    def value(self):
        return self.stats['value']

    @property
    def revealed(self):
        return self._revealed and self.visible

    def reveal(self):
        self._revealed = True

    def tick_time(self):
        try:
            self._time -= 1
            if self._time < 1:
                self.remove()
        except TypeError:
            pass


class HomeWorld(object):

    def __init__(self, id):
        self.id = id
        self.data = store.homeworlds_dict[id]
        self._description = self._get_description()

    def name(self):
        return self.data.get("name", 'No name')

    def _get_description(self):
        return choice(self.data['descriptions'])

    @property
    def tags(self):
        return self.data.get('tags', list())

    def description(self):
        return self._description
