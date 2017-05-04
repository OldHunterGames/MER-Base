# -*- coding: UTF-8 -*-
from random import choice

from mer_utilities import weighted_random

import renpy.store as store


_available_ages_ = ['junior', 'adolescent', 'mature', 'elder']


def available_genuses():
    return [name for name in store.genuses_data.keys()]


class Genus(object):
    _available_ages = ['adolescent', 'mature']
    _available_genders = ['male', 'female', 'sexless', 'shemale']

    def __init__(self, id_):
        self.id = id_
        self.data = store.genuses_data[id_]

    def __getattr__(self, key):
        try:
            value = self.__dict__['data'][key]
        except KeyError:
            raise AttributeError(key)
        return value

    def count_modifiers(self, attr):
        return self.data.get('modifiers', 0).get(attr, 0)

    def description(self):
        return self.data.get('description', 'No description')

    def apply(self, person):
        func = self.data.get('on_apply')
        if func is not None:
            func(person)

    def remove(self, person):
        func = self.data.get('on_remove')
        if func is not None:
            func(person)

    def get_face_type(self):
        return self.data.get('head_type', 'human')

    def genders(self):
        try:
            genders = self.data['genders']
        except KeyError:
            genders = self._available_genders
        return genders

    def get_gender(self):
        try:
            gender = weighted_random(self.genders)
        except ValueError:
            gender = choice(self.genders)
        return gender

    def genders_names(self):
        return [i[0] for i in self.genders]

    def get_age(self):
        try:
            age = weighted_random(self.ages)
        except ValueError:
            age = choice(self.ages)
        return age

    def ages(self):
        try:
            ages = self.data['ages']
        except KeyError:
            ages = self._available_ages
        return ages

    def ages_names(self):
        return [i[0] for i in self.ages]

    @property
    def head_type(self):
        return self.data['head_type']

    def features(self):
        try:
            features = self.data['features']
        except KeyError:
            features = []
        return features

    @property
    def name(self):
        return self.data['name']

    @property
    def type(self):
        return self.data['type']

    def get_quirk(self, value=None):
        return self.data.get('quirk', value)

    def get_appearance(self, value=None):
        return self.data.get('appearance', value)

    def get_shape(self, value=None):
        return self.data.get('shape', value)

    def get_constitution(self, value=None):
        return self.data.get('constitution', value)

    @property
    def tags(self):
        return self.data.get('tags', list())
