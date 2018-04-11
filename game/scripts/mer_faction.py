# -*- coding: <UTF-8> -*-
from collections import defaultdict


class Occupation(object):
    OCCUPATIONS = dict()

    @staticmethod
    def get_occupation(person):
        return Occupation.OCCUPATIONS.get(person)

    def __init__(self, data):

        self._data = data
        self._employees = dict()

    def add_employee(self, person):
        self._employess[person] = 1
        self.OCCUPATIONS[person] = self

    def remove_employee(self, person):
        del self._employess[person]
        del self.OCCUPATIONS[person]

    def available(self, person):
        if self.gengder() is None:
            return True
        else:
            return self.gengder() == person.gender

    def level(self, person):
        return self._employess.get(person, 0)

    def promote(self, person):
        if self.level(person) < 5:
            self._employess[person] += 1

    def name(self):
        return self._data.get('name')

    def attribute(self):
        return self._data.get('attribute')

    def gender(self):
        return self._data.get('gender')


class CoreFaction(object):

    ROLE_LEADER = 3
    ROLE_TOP = 2
    ROLE_LOW = 1

    FACTIONS = {}

    @staticmethod
    def get_faction(person):
        return CoreFaction.FACTIONS.get(person)

    def __init__(self, id, data, occupations=None):
        self._id = id
        self._data = data
        self._members = defaultdict(list)
        if occupations is None:
            self._occupations = list()
        else:
            self._occupations = occupations

    def roles_data(self):
        return self._data.get('roles', dict())

    @property
    def id(self):
        return self._id

    def can_be_member(self, person):
        func = self._data.get('check_person', lambda x: True)
        return func(person)

    def add_member(self, person, role):
        self._members[role].append(person)
        self.FACTIONS[person] = self

    def name(self):
        return self._data.get('name', 'No name')

    def description(self):
        return self._data.get('description', 'No description')

    def available_for_communication(self):
        available = list()
        roles = self.roles_data()
        for key, value in self._members.items():
            if roles.get(key, self.ROLE_LOW) == self.ROLE_LOW:
                available.extend(value)
        return available