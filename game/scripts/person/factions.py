# -*- coding: UTF-8 -*-


class Faction(object):
    _max_ingrigues = 3

    def __init__(self, owner):
        self._size = 15
        self._slots = []
        self.add_member(owner)

    def add_member(self, person):
        slots = self._slots
        if len(slots) == 15:
            raise Exception("Faction can't handle more members")
        person.die.add_callback(self._remove_member_callback)
        self._slots.append(person)

    def get_members(self):
        return sorted(self._slots,
                      key=lambda person: self.get_influence(person))

    def has_slots(self):
        return len(self._slots) < 15

    def get_influence(self, person):
        return 0

    def _remove_member_callback(self, person, *args):
        self.remove_member(person)

    def remove_member(self, person):
        try:
            self._slots.remove(person)
        except ValueError:
            pass

    def make_intrigues(self):
        pass

    def get_frame_color(self, person):
        return '#00ff00'
