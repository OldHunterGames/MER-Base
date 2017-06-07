# -*- coding: UTF-8 -*-
import renpy.store as store


class Faction(object):
    _max_ingrigues = 3

    def __init__(self, owner):
        self._size = 15
        self._slots = dict()
        self.add_member('king', owner)

    def add_member(self, slot, person):
        slots = self._slots.keys()
        if slot not in slots and len(slots) == 15:
            raise Exception("Faction can't handle more members")
        person.die.add_callback(self._remove_member_callback)
        self._slots[slot] = person

    def has_slots(self):
        return len(self._slots.keys()) < 15

    def get_influence(self, person):
        return 0

    def _remove_member_callback(self, person, *args):
        self.remove_member(person)

    def remove_member(self, person):
        for key, value in self._slots.items():
            if value == person:
                person.die.remove_callback(self._remove_member_callback)
                self._remove_member(key)
                return

    def _remove_member(self, slot):
        try:
            del self._slots[slot]
        except KeyError:
            pass

    def make_intrigues(self):
        pass

    def framed_avatar(self, person):
        return person.avatar
