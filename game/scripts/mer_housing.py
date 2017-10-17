# -*- coding: UTF-8 -*-
import copy
import renpy.store as store
from schedule import ScheduleObject


class Housing(object):

    def __init__(self):
        self._dwellers = dict()

    def add_dweller(self, person, house):
        self._dwellers[person] = house

    def remove_dweller(self, person):
        try:
            del self._dwellers[person]
        except KeyError:
            pass

    @staticmethod
    def get_house(id):
        data = store.housing_data.get(id)
        cls = globals()[data.get('house_type').capitalize()]
        return cls(data, id)


class HouseType(object):

    def __init__(self, data, id):
        self.id = id
        self._data = data
        self._used_accommodations = list()
        self._accommodations = self._init_accommodations()

    def name(self):
        return self._data.get('name', 'No name')

    def description(self):
        return self._data.get('description', "No description")

    def available_accommodations(self):
        return [i for i in self._accommodations if i not in self._used_accommodations]

    def _init_accommodations(self):
        accommodations = list()
        for id, data in self._data.get('accommodations', list()):
            data = getattr(store, data)
            accommodations.append(ScheduleObject(id, data))
        return accommodations

    def cost(self):
        return self._data.get('cost', 0)

    def used_accommodations(self):
        return copy.copy(self._used_accommodations)

    # every house has limited slots for our slaves
    def use_accommodation(self, accommodation):
        self._used_accommodations.append(accommodation)

    def free_accommodations(self, accommodation):
        self._used_accommodations.remove(accommodation)

    def available(self, person):
        # every house is available by default
        return True


class Hostel(HouseType):
    pass
