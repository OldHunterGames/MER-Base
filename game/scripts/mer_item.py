# -*- coding: <UTF-8> -*-
from random import *

import renpy.store as store
import renpy.exports as renpy

from features import Feature
from modifiers import Modifiable
from mer_utilities import encolor_text, empty_card

# sizes 'offhand', 'versatile', 'shield', 'twohand'


class Item(Modifiable):
    type_ = 'item'

    def __init__(self, id_, data_dict):
        self.data = data_dict[id_]
        self.id = id_
        self.equiped = False
        self.init_modifiable()

        self.features = []
        self.features_data_dict = 'item_features'

        self.new_description = None
        self.new_name = None

    def has_tag(self, tag):
        return tag in self.data['tags']

    def count_modifiers(self, attribute):
        value = super(Item, self).count_modifiers(attribute)
        for i in self.features:
            value += i.count_modifiers(attribute)
        return value

    def sellable(self):
        return self.price > 0

    @property
    def price(self):
        return self.data.get('price', 1)

    @property
    def quality(self):
        value = self.data.get('quality', 0)
        value += self.count_modifiers('quality')
        return max(0, min(5, value))

    def set_quality(self, quality):
        self._quality = quality

    def name(self):
        if self.new_name is not None:
            return self.new_name
        name = self.data.get('name', 'Unnamed')
        return name

    def colored_name(self):
        return encolor_text(self.name(), self.quality)

    @property
    def mutable_name(self):
        return self.data.get('mutable_name', False)

    def set_name(self, name):
        if not self.mutable_name:
            return
        self.new_name = name

    def reset_name(self):
        self.new_name = None

    @property
    def type(self):
        return self.type_

    @property
    def amount(self):
        return 1

    def description(self):
        return self.name() # temporary
        if self.new_description is not None:
            return self.new_description
        return self.data.get('description', "No description")

    def set_description(self, value):
        if not self.mutable_description:
            return
        self.new_description = value

    @property
    def mutable_description(self):
        return self.data.get('mutable_description', False)

    def reset_description(self):
        self.new_description = None

    def add_feature(self, id_):
        self.features.append(Feature(id_, self.features_data_dict))

    def remove_feature(self, feature):
        if isinstance(feature, str):
            for i in self.features:
                if i.id == feature:
                    self.features.remove(i)
        else:
            try:
                self.features.remove(feature)
            except ValueError:
                return

    def feature_by_slot(self, slot):
        for feature in self.features:
            if feature.slot == slot:
                return feature

    def use(self):
        return

    def equip(self):
        self.equiped = True

    def unequip(self):
        self.equiped = False

    def stats(self):
        return ''

    def stackable(self):
        return False

    @property
    def present(self):
        return self.data.get('present', None)

    def image(self):
        return self.data.get('image', empty_card())

    @property
    def tags(self):
        return self.data.get('tags', list())
