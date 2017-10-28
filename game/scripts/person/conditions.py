# -*- coding: UTF-8 -*-
import renpy.store as store
from modifiers import ModifiersStorage, Modifier
from mer_command import Skillcheck
from mer_utilities import empty_card
import random
import copy


def make_condition(id, data_dict, time):
    cls_name = data_dict[id].get('cls_name', "PersonCondition")
    return globals()[cls_name](id, data_dict, time)


class ConditionsMaker(object):

    def __init__(self, conditions_maker=None, **kwargs):
        if conditions_maker is not None:
            self._data = conditions_maker.get_data()
        else:
            self._data = dict()

        self.add_data(kwargs)

    def add_data(self, dict_):
        self._data.update(dict_)

    def get_data(self):
        return copy.copy(self._data)

    def make_condition(self, id, time=1):
        cond_data = self._data[id]
        cls_name = cond_data.get('cls_name', 'PersonCondition')
        return globals()[cls_name](id, cond_data, time)

    def make_conditions(self, type, time):
        conditions = list()
        for key, value in self._data.items():
            if value.get('type') == type:
                conditions.append(key)
        return [self.make_condition(i, time) for i in conditions]


class PersonCondition(ModifiersStorage):

    def __init__(self, id_, data_dict, time=1, *args, **kwargs):
        self.data = data_dict
        self.id = id_
        self._time = time
        self._modifiers = []
        if self._get_modifiers_data() is not None:
            self.add_modifier(
                self.name(), self._get_modifiers_data(), self, self.slot())

    def check_modifiers(self):
        return self.data.get('check_modifiers', 0)

    def on_add(self, person):
        "Called on adding condition to a person"
        # override this in child classes if needed
        return

    def on_remove(self, person):
        "Called on removing condition from a person"
        # override this in child classes
        return

    def type(self):
        return self.data.get('type')

    def slot(self):
        return self.data.get('slot', self.id)

    def name(self):
        return self.data.get('name', 'No name')

    def description(self):
        return self.data.get('description', 'No description')

    def image(self):
        return empty_card()

    def _get_modifiers_data(self):
        return self.data.get('modifiers')

    def tick_time(self):
        self._time -= 1

    def ended(self):
        if this._time is None:
            return False
        return 0 > this._time

    def add_modifier(self, name, stats_dict, source, slot=None):
        self._modifiers.append(Modifier(name, stats_dict, self, slot))

    def get_all_modifiers(self):
        return self._modifiers


class SuicidalCondition(PersonCondition):

    def _rest_callback(self, person, *args, **kwargs):
        # some selfdestructing event here
        person.remove_condition(self)
        return

    def on_add(self, person):
        person.rest.add_callback(self._rest_callback)

    def on_remove(self, person):
        person.rest.remove_callback(self._rest_callback)

    def additional_ended(self):
        return False


class MisstepCondition(PersonCondition):

    def on_add(self, person):
        self.__person = person
        Skillcheck.run.add_callback(self.__skillcheck_callback)

    def on_remove(self, person):
        Skillcheck.run.remove_callback(self.__skillcheck_callback)

    def __skillcheck_callback(self, skillcheck, *args, **kwargs):
        print 'Misstep is gone'
        if skillcheck.person == self.__person:
            self.__person.remove_condition(self)
            return


class HesistationCondition(PersonCondition):

    def on_add(self, person):
        attr = random.choice(store.person_attributes.keys())
        self.add_modifier(Modifier(self.name(), {attr: -1}, self, self.slot()))

    def __satisfy_callback(self, person, *args, **kwargs):
        name = args[0]
        if name == 'ambition':
            person.remove_condition(self)

    def on_remove(self, person):
        person.satisfy_need.remove_callback(self.__satisfy_callback)

