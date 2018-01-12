# -*- coding: UTF-8 -*-
from mer_person import PersonCreator
from mer_actions import Actions
from schedule import ScheduleObject, ScheduleJob
from wishes import WishesGenerator
from collections import defaultdict
from mer_housing import Housing
from conditions import ConditionsMaker
import random
import renpy.exports as renpy
import renpy.store as store
import copy


class MERCore(object):

    def __init__(self):

        self._player = None
        self._world = 'core'
        self._journal = EventsBook()
        self._active_npcs = set()
        self._personized_journal = PersonalBook()
        self.wish_maker = WishesGenerator()
        self.person_creator = PersonCreator()
        self._housing = Housing()
        self.conditions_maker = ConditionsMaker(**store.conditions_data)
        self.actions = Actions()

    def call_screen(self, screen_name, *args, **kwargs):
        renpy.call_screen(screen_name, *args, **kwargs)

    def get_house(self, id):
        return self._housing.get_house(id)

    def add_dweller(self, person, house):
        self._housing.add_dweller(person, house)

    def dweller_house(self, person):
        return self._housing.dweller_house(person)

    def remove_dweller(self, person):
        self._housing.remove_dweller(person)

    def _find_phantoms(self):
        actives = set(self.get_active_persons())
        actives.add(self.player)
        phantoms = set()
        for i in actives:
            phantoms.update(
                set(i.known_characters()).difference(actives))
        return phantoms

    def get_phantom(self):
        phantoms = self._find_phantoms()
        if len(phantoms) > 0:
            return random.choice(list(phantoms))

    def get_active_persons(self, exclude=None):
        npcs = list(self._active_npcs)
        npcs.extend(self._player.known_characters())
        if exclude is not None:
            npcs.remove(exclude)
        return npcs

    def process_wishes(self):
        return
        for i in self.get_active_persons():
            self.wish_maker.process_wishes(i)

    def process_bonds(self):
        for i in self.get_active_persons():
            bonds = i.get_bonds()
            for n in range(0, i.occupation_level) and len(bonds) > 0:
                bond = random.choice(bonds)
                bonds.remove(bond)
                bond.target.resources_bonus += 1

    def process_resources(self):
        for person in self.get_active_persons():
            if person.resources_bonus > 0:
                for i in range(0, person.resources_bonus):
                    try:
                        resource = random.choice(
                            [r for r in person.resources() if person.resource(r) < 5])
                    except IndexError:
                        person.resources_bonus = 0
                    else:
                        person.add_resource(resource, 1)
            elif person.resources_bonus < 0:
                for i in range(0, abs(person.resources_bonus)):
                    try:
                        resource = random.choice(
                            [r for r in person.resources() if person.resource(r) > 0])
                    except IndexError:
                        person.resources_bonus = 0
                    else:
                        person.use_resource(resource, 1)
            person.resources_bonus = 9

    def add_record(self, value):
        self._journal.add_entry(value)

    def get_records(self):
        return self._journal.get_records()

    def add_personal_record(self, person, value):
        self.add_record(value)
        self._personized_journal.add_entry(person, value)

    def get_personal_records(self, person):
        return self._personized_journal.get_records(person)

    @property
    def player(self):
        return self._player

    def set_player(self, person):
        self._player = person
        house = self._housing.get_house('inn')
        self._housing.add_dweller(person, house)
        person.player_controlled = True

    def reveal_npc(self, person):
        self._active_npcs.add(person)

    def set_world(self, world):
        self._world = world
    
    @property
    def world(self):
        return self._world

    def skip_turn(self):
        self._journal.skip_turn()
        self.process_wishes()
        self._player.rest()
        self._player.tick_time()
        renpy.call_in_new_context('lbl_turn_end')

    def can_skip_turn(self):
        return self._player.can_tick()

    def create_player(self):
        player = PersonCreator().gen_random_person()
        self.set_player(player)
        player.civil_income = 100

    def unlock_schedule(self, person):
        basic_schedule = {
            'job': store.basic_jobs,
            'ration': store.basic_rations,
            'extra': store.basic_extras}
        for key, data in basic_schedule.items():
            for i in data:
                if key == 'job':
                    person.schedule.add_available(ScheduleJob(i, data))
                else:
                    person.schedule.add_available(ScheduleObject(i, data))


class EventsBook(object):

    def __init__(self, turns_to_store=0):
        self._events = list()
        self._turns_to_store = turns_to_store
        self._turns_passed = 0

    def skip_turn(self):
        self._turns_passed += 1
        if self._turns_passed > self._turns_to_store:
            self._clear_events()
            self._turns_passed = 0

    def _clear_events(self):
        self._events = list()

    def add_entry(self, value):
        self._events.append(value)

    def get_records(self):
        return copy.copy(self._events)


class PersonalBook(EventsBook):

    def __init__(self, turns_to_store=0):
        super(PersonalBook, self).__init__(turns_to_store)
        self._events = defaultdict(list)

    def add_entry(self, person, value):
        self._events[person].append(value)

    def get_records(self, person):
        return copy.copy(self._events[person])

    def _clear_events(self):
        self._events = defaultdict(list)


class World(object):
    # Basic class for every world connected to MER
    # in modules, save any specific data to world instance
    # to save state between visits to same world
    
    items_whitelist = []
    description = None
    type = None

    def __init__(self):
        self._travelers = list()
    
    def _transfer_persons(self, *args):
        #basic implementation for persons transfering between worlds
        #for i in args:
        #    self._transfer_items(i)
        self._travelers += args
    
    def _transfer_items(self, person):
        # basic implementation for items transfering
        for item in person.all_items():
            if item.id not in self.items_whitelist:
                person.remove_item(item)
    
    def entry_point(self):
        # should return entry label of world
        raise NotImplementedError
    
    def return_point(self):
        return None

    def travel(self, core, travelers):
        core.set_world(self)
        self._transfer_persons(*travelers)
        if getattr(self, '__visited', False):
            if self.return_point() is not None:
                renpy.call_in_new_context(self.return_point(), world=self)
        self.__visited = True
        renpy.call_in_new_context(self.entry_point(), world=self)
    
    @classmethod
    def can_create_worlds(cls):
        return True
    
    @classmethod
    def get_worlds(cls):
        return [i for i in cls.__subclasses__() if i.can_create_worlds]


class MistTravel(object):


    def __init__(self, core, world_cls, *args):
        self.core = core
        self.world = world_cls()
        self.travelers = args
    
    def travel(self):
        #TODO: mist events
        self.world.travel(self.core, self.travelers)
        # mist event again
        self.core.set_world('core')
        #TODO: clear outer world items

