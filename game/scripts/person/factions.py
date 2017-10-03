# -*- coding: UTF-8 -*-
import random
import renpy.store as store


class Faction(object):
    _max_ingrigues = 3

    def __init__(self, owner):
        self._slots = dict()
        self.add_member(owner, role='leader')

    @property
    def max_intrigues(self):
        return self._max_ingrigues

    def add_member(self, person, role='patrician'):
        # adds member, each role but pratician is unique
        # if faction have this role, sets new member to it and
        # old member to patrician
        if role != 'patrician' and role in self._slots.values():
            old_person = self._remove_role(role)
            self.add_member(old_person)
            return
        person.occupation = random.choice(store.faction_occupations.keys())
        person.occupation_level = 1
        person.die.add_callback(self._remove_member_callback)
        self._slots[person] = role
        person.set_faction(self)

    def _remove_role(self, role):
        for person, r in self._slots.items():
            if r == role:
                self.remove_member(person)
                return person

    def get_members(self, sort=False):
        return self._slots.keys()

    def _remove_member_callback(self, person, *args):
        self.remove_member(person)

    def remove_member(self, person):
        try:
            del self._slots[person]
        except KeyError:
            pass
