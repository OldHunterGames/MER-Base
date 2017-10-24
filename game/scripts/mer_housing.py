# -*- coding: UTF-8 -*-
import copy
import renpy.store as store
from schedule import Schedule, ScheduleObject, ExternController


class Housing(object):

    def __init__(self):
        self._dwellers = dict()
        self._controllers = dict()

    def dweller_house(self, person):
        return self._dwellers.get(person)

    def add_dweller(self, person, house):
        if person in self._dwellers.keys():
            self.remove_dweller(person)
        self._dwellers[person] = house
        controller = ExternController(
            house.available_accommodations,
            house.use_accommodation,
            house.free_accommodation,
            house.accommodations
        )
        person.schedule.extern_available(
            Schedule.ACCOMMODATION,
            controller
        )
        self._controllers[person] = controller

    def remove_dweller(self, person):
        try:
            del self._dwellers[person]
            person.schedule.unextern_available(
                Schedule.ACCOMMODATION, self._controllers[person])
            del self._controllers[person]
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

    def accommodations(self):
        return copy.copy(self._accommodations)

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

    def free_accommodation(self, accommodation):
        self._used_accommodations.remove(accommodation)

    def available(self, person):
        # every house is available by default
        return True


class Hostel(HouseType):
    pass
