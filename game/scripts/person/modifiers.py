import collections


class Modifier(object):
    """Used to modify any numeric attribute of holder"""

    def __init__(self, name, stats, source, slot=None):
        self.name = name
        self.stats = stats
        self.source = source
        self.slot = slot

    def value(self, attr):
        return self.stats.get(attr, 0)

    def description(self):
        pass


class ModifiersStorage(object):

    def count_modifiers(self, attribute):
        return sum(
            [i.value(attribute) for i in self.get_all_modifiers()])

    def remove_modifier(self, source):
        raise NotImplementedError

    def get_all(self):
        return [mod.description for mod in self.get_all_modifiers()]

    def add_modifier(self, name, stats_dict, source, slot=None):
        raise NotImplementedError

    def get_all_modifiers(self):
        # should return collecton of Modifier instances
        raise NotImplementedError


class Modifiable(object):
    # Interface for modifiable objects
    # maybe rewrite this as fully interface-like class
    # without init 'dirty' hack?
    def init_modifiable(self):
        self._modifiers = ModifiersStorage()

    def remove_modifier(self, source):
        self._modifiers.remove_modifier(source)

    def add_modifier(self, id_, stats_dict, source, slot=None):
        self._modifiers.add_modifier(id_, stats_dict, source, slot)

    def count_modifiers(self, key):
        # any numeric attribute can be modified with modifiers
        # should be used in attribute get func or property
        val = self.__dict__['_modifiers'].count_modifiers(key)
        return val

    def modifiers_separate(self, modifier):
        # obsolete?
        return self._modifiers.get_modifier_separate(modifier)

    def get_all_modifiers(self):
        return self._modifiers.get_all_modifiers()
