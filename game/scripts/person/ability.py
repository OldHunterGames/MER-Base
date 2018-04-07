# -*- coding: <UTF-8> -*-
import renpy.store as store
import renpy.exports as renpy
    

class Ability(object):

    ABILITIES = {}

    def __init__(self, data):
        self._data = data

    def add(self, person, prev_ability):
        lbl = self._data.get('on_add')
        if lbl is not None:
           return renpy.call_in_new_context(lbl, person, self, prev_ability)

    def count_modifiers(self, attr):
        return self._data.get('modifiers', {}).get(attr, 0)

    def name(self):
        return self._data.get('name', '')

    def description(self):
        return self._data.get('description', '')

    @staticmethod
    def make_abilities(dict_):
        for key, value in dict_.items():
            Ability.ABILITIES[key] = Ability(value)

    @staticmethod
    def get_ability(id):
        return Ability.ABILITIES.get(id)