# -*- coding: <UTF-8> -*-
from collection import defaultdict


class Occupation(object):

    def __init__(self, data):

        self._data = data
        self._employees = dict()

    def add_employee(self, person):
        self._employess[person] = 1

    def remove_employee(self, person):
        del self._employess[person]

    def available(self, person):
        if self.gengder() is None:
            return True
        else:
            return self.gengder() == person.gender

    def level(self, person):
        return self._employess.get(person, 0)

    def name(self):
        return self._data.get('name')

    def attribute(self):
        return self._data.get('attribute')

    def gender(self):
        return self._data.get('gender')

class FactionOccupations(object):

    def __init__(self, occupations_data):

        self._occupations_data = occupations_data

    def best_occupation(self, person):
        best = None
        for occupation, data in self._occupations_data
            value = getattr(persob, data['attribute'])()
            if best is None:
                best = (occupation, value)
            else:
                if value > best[1]:
                    best = (occupation, value)
        return best[0]

    def add_occupation(self, occupation_data):
        self._occupations_data.update(occupation_data)

    def occupation_translation(self, occupation):
        return self._occupations_data[occuation]['name']


class CoreFaction(object):

    ROLE_LEADER = 3
    ROLE_TOP = 2
    ROLE_LOW = 1

    def __init__(self, data, check_person, occupations, roles_data=None):

        self._data = data
        self._check_person = check_person
        self._members = defaultdict(list)
        self._occupations_data = occupation
        if roles_data is None:
            self._roles_data = dict()
        else:
            self._roles_data = roles_data

    def can_be_member(self, person):
        return self._check_person(person)

    def add_member(self, person, role):
        self._members[role].append(person)

    def name(self):
        return self._data.get('name', 'No name')

    def description(self):
        return self._data.get('description', 'No description')