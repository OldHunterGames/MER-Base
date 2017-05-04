# -*- coding: UTF-8 -*-
import collections
import copy
from mer_itemsstorage import ItemsStorage
from modifiers import ModifiersStorage
import mer_utilities as utilities
from mer_item import Item
import renpy.store as store


class ItemSlot(object):

    def __init__(self, default):

        self._current = None
        self._default = default
        self._blocked = False

    @property
    def current(self):
        return self._current

    @property
    def default(self):
        return self._default

    def set_default(self, item):
        self._default = item

    def get_item(self):
        if self._current is None:
            return self._default
        return self._current

    def set_item(self, item):
        if self._current is not None:
            self._current.unequip()
        self._current = item
        if item is not None:
            item.equip()

    def allowed(self, item):
        raise NotImplementedError()

    def block(self):
        self._blocked = True

    def unlock(self):
        self._blocked = False

    @property
    def blocked(self):
        return self._blocked

    def count_modifiers(self, attr):
        if self.get_item() is None:
            return 0
        else:
            return self.get_item().count_modifiers(attr)


class MainImplement(ItemSlot):

    def __init__(self, default):
        super(MainImplement, self).__init__(default)
        # self.block()

    def allowed(self, item):
        tags = ['heavy', 'versatile', 'offhand']
        return any([i in item.tags for i in tags])


class SecondaryImplement(MainImplement):

    def allowed(self, item):
        tags = ['versatile', 'shield', 'offhand']
        return any([i in item.tags for i in tags])


class ArmorSlot(ItemSlot):

    def allowed(self, item):
        tags = ['garments', 'soft_armor', 'hard_armor']
        return any([i in item.tags for i in tags])


class AccessorySlot(ItemSlot):

    def allowed(self, item):
        tags = ['accessory', 'offhand']
        return any([i in item.tags for i in tags])


class LoadSlot(ItemSlot):

    def allowed(self, item):
        return True

    def count_modifiers(self, attr):
        if self.get_item() is not None:
            if ('accessory' in self.get_item().tags or
                    'load' in self.get_item().tags):
                return self.get_item().count_modifiers(attr)
        return 0


class Inventory(ItemsStorage, ModifiersStorage):

    def __init__(self):
        super(Inventory, self).__init__()
        self._slots = collections.OrderedDict(
            [
                ('main_implement', MainImplement(None)),
                ('secondary_implement', SecondaryImplement(None)),
                ('garment', ArmorSlot(None)),
                ('main_accessory', AccessorySlot(None)),
                ('secondary_accessory', AccessorySlot(None)),
                ('load', LoadSlot(None))

            ]
        )
        # self._main_hand = self._slots['weapon']
        # self._other_hand = self._slots['weapon2']
        self.storage = []
        self.money = 0

    def slots(self):
        return copy.copy(self._slots)

    def available_for_slot(self, slot, storage=None):
        if storage is None:
            storage = self.unequiped_items()
        slot = self._slots[slot]
        return [i for i in storage if slot.allowed(i)]

    def count_modifiers(self, attr):
        return sum(
            [i.count_modifiers(attr) for i in self._slots.values()])

    def get_slot(self, key):
        return self._slots.get(key, ItemSlot(None))

    def remove_modifier(self, source):
        pass

    def equiped_items(self):
        return [i for i in self.storage if i.equiped]

    def all_items(self):
        return [i for i in self.storage]

    def unequiped_items(self):
        return [i for i in self.storage if not i.equiped]

    def armor_slots(self):
        return self.carried_armor.keys()

    @property
    def main_hand(self):
        return self._main_hand.get_item()

    @main_hand.setter
    def main_hand(self, weapon):
        if weapon == self._main_hand.get_item():
            return
        self.disarm_weapon('main_hand')
        if weapon is None:
            return
        self.add_item(weapon)
        weapon.equip()

        if weapon.size == 'twohand':
            self.disarm_weapon('other_hand')
            self._other_hand.set_item(weapon)
        self._main_hand.set_item(weapon)

    @property
    def other_hand(self):
        return self._other_hand.get_item()

    @other_hand.setter
    def other_hand(self, weapon):
        if weapon == self._other_hand.get_item():
            return
        self.disarm_weapon('other_hand')
        if weapon is None:
            return
        if weapon.size == 'twohand':
            self.disarm_weapon('main_hand')
            self._main_hand.set_item(weapon)
        self._other_hand.set_item(weapon)

    def weapons(self):
        return [self._slots['main_implement'].get_item(),
                self._slots['secondary_implement'].get_item()]

    def equip_on_slot(self, slot, item):
        if item not in self.storage and item is not None:
            self.add_item(item)
        dict_ = self._slots
        if item == dict_[slot].get_item():
            return
        dict_[slot].set_item(item)

        if slot == 'main_implement':
            if item is None:
                dict_['secondary_implement'].unlock()
                return
            if 'heavy' in item.tags:
                dict_['secondary_implement'].set_item(None)
                dict_['secondary_implement'].block()
            else:
                dict_['secondary_implement'].unlock()
        if slot == 'garments':
            if item is None:
                dict_['secondary_accessory'].unlock()
            if 'hard_armor' in item.tags:
                dict_['secondary_accessory'].set_item(None)
                dict_['secondary_accessory'].block()
            else:
                dict_['secondary_accessory'].unlock()

    def equip_weapon(self, weapon, hand='main_hand'):
        if weapon is not None:
            weapon.equip()
            if weapon.size == 'twohand':
                self.main_hand = weapon
                self.other_hand = weapon
            else:
                other = 'other_hand' if hand == 'main_hand' else 'main_hand'
                try:
                    if getattr(self, other).size == 'twohand':
                        setattr(self, other, create_item('bare_hands', 'weapon'))
                except AttributeError:
                    pass
        getattr(self, '_' + hand).set_item(weapon)

    def in_hands(self, item):
        if self.main_hand == item or self.other_hand == item:
            return True
        return False

    def remove_item(self, item, value=1, return_item=True):
        get_item = None
        if isinstance(item, str):
            for i in self.storage:
                if i.id == item:
                    get_item = i
                    break
        else:
            for i in self.storage:
                if i == item:
                    get_item = i
                    break
        if get_item is not None:
            if get_item.stackable():
                returned = get_item.decrease_amount(value)
                if get_item.amount <= 0:
                    self.storage.remove(get_item)
            else:
                self.storage.remove(get_item)
                returned = get_item
        for value in self._slots.values():
            if value.current == item:
                value.set_item(None)
                item.unequip()
        if self.main_hand == item:
            self.main_hand = None
        if self.other_hand == item:
            self.other_hand = None
        if return_item:
            return returned


class InventoryWielder(object):

    def init_inventorywielder(self):
        self.inventory = Inventory()
        self.corpse_storage = []
        self.corpse_buffer = None

    def any_equiped(self):
        return any(self.equiped_items())

    def slot_active(self, slot):
        # if slot == 'main_implement' or slot == 'secondary_implement':
        #     return (self.has_body_part('manipulators') and
        #             not self.inventory.slots()[slot].blocked)
        return not self.inventory.slots()[slot].blocked

    @property
    def trade_level(self):
        return self.inventory.trade_level

    @trade_level.setter
    def trade_level(self, value):
        self.inventory.trade_level = value

    @property
    def money(self):
        return self.inventory.money

    @money.setter
    def money(self, value):
        self.inventory.money = value

    def add_money(self, value):
        self.inventory.add_money(value)

    def remove_money(self, value):
        self.inventory.remove_money(value)

    def has_money(self, value):
        return self.inventory.has_money(value)

    def transfer_money(self, storage, value):
        self.inventory.transfer_money(storage, value)

    @utilities.Observable
    def add_corpse(self, person):
        self.corpse_storage.append(person)

    @utilities.Observable
    def remove_corpse(self, person):
        self.corpse_storage.remove(person)

    def get_best_corpse(self):
        if len(self.get_corpses()) < 1:
            return -1
        else:
            if self.corpse_buffer is not None:
                return self.corpse_buffer.succulence()
            return max([i.succulence() for i in self.get_corpses()])

    def get_corpses(self):
        corpses = [i for i in self.corpse_storage]
        if self.corpse_buffer is not None:
            corpses.append(self.corpse_buffer)
        return corpses

    def eat_corpse(self, corpse):
        self.satisfy_need('nutrition', corpse.succulence())
        canibalism = self.schedule.get('ration', 'canibalism')
        canibalism.lock()
        self.schedule.set('ration', canibalism)
        self.corpse_buffer = corpse
        self.remove_corpse(corpse)

    def decay_corpses(self):
        self.corpse_buffer = None
        for i in [c for c in self.corpse_storage]:
            self.remove_corpse(i)

    def equiped_items(self):
        return self.inventory.equiped_items()

    @property
    def items(self):
        return self.inventory.items

    def unequiped_items(self):
        return self.inventory.unequiped_items()

    @property
    def main_hand(self):
        return self.inventory.main_hand

    @main_hand.setter
    def main_hand(self, weapon):
        self.inventory.main_hand = weapon

    @property
    def other_hand(self):
        return self.inventory.other_hand

    @other_hand.setter
    def other_hand(self, weapon):
        self.inventory.other_hand = weapon

    @property
    def armor(self):
        return self.inventory.get_slot('garment').current

    @armor.setter
    def armor(self, armor):
        self.inventory.equip_armor(armor, 'garment')

    def has_shield(self):
        try:
            main = self.inventory.main_hand
            other = self.inventory.other_hand
            if main.size == 'shield' or other.size == 'shield':
                return True
        except AttributeError:
            pass
        return False

    def equip_weapon(self, weapon, hand='main_hand'):
        self.inventory.equip_weapon(weapon, hand)

    def disarm_weapon(self, hand='main_hand'):
        self.inventory.disarm_weapon(hand)

    def equip_armor(self, item, slot):
        self.inventory.equip_armor(item, slot)

    def equip_item(self, item, slot):
        if item.type == 'armor':
            self.equip_armor(item, slot)
        elif item.type == 'weapon':
            self.equip_weapon(item, slot)

    def available_for_slot(self, slot):
        return self.inventory.available_for_slot(slot)

    def equip_on_slot(self, slot, item):
        self.inventory.equip_on_slot(slot, item)

    def weapons(self):
        return self.inventory.weapons()

    def has_item(self, item):
        return self.inventory.has_item(item)

    def remove_item(self, item, value=1, return_item=True):
        return self.inventory.remove_item(item, value, return_item)

    def add_item(self, item, value=1):
        self.inventory.add_item(item, value)

    def weapon_slots(self):
        return self.inventory.weapon_slots()

    def get_items(self, item_type):
        return self.inventory.get_items(item_type)

    @property
    def carried_weapons(self):
        return self.inventory.carried_weapons

    def transfer_item(self, item, storage, value=1):
        self.inventory.transfer_item(item, storage, value)

    def transfer_all(self, storage):
        self.inventory.transfer_all(storage)

    def get_slot(self, slot):
        return self.inventory.get_slot(slot)

    def has_items(self):
        return len(self.inventory.items) > 0

    def all_items(self):
        return self.inventory.items
