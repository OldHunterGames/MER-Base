# -*- coding: UTF-8 -*-

from modifiers import ModifiersStorage, Modifier

def make_condition(id, data_dict, time):
    cls_name = data_dict.get('cls_name', "PersonCondition")
    return globals()[cls_name](id, data_dict, time)

class PersonCondition(ModifiersStorage):

    def __init__(self, id_, data_dict, time=1, *args, **kwargs):
        self.data = data_dict[id_]
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
        return self.data.get('slot')

    def name(self):
        return self.data.get('name', 'No name')

    def _get_modifiers_data(self):
        return self.data.get('modifiers')

    def tick_time(self):
        self._time -= 1

    def ended(self):
        return self._time > 0 and self.additional_ended()

    def additional_ended(self):
        "Special rules for ending this condition or block ending this on time"
        return True

    def add_modifier(self, name, stats_dict, source, slot=None):
        self._modifiers.append(Modifier(name, stats_dict, self, slot))

    def get_all_modifiers(self):
        return self._modifiers

    def modify_check(self, value):
        """
        Modifies value of skillcheck, returns tuple(value, bool) where bool
        determines if we should stop modifying
        """
        # override this in child classes
        return (value + self.check_modifiers(), False)


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