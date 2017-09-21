# -*- coding: UTF-8 -*-
from mer_person import PersonCreator
from schedule import ScheduleObject, ScheduleJob
from wishes import WishesGenerator
import random
import renpy.exports as renpy
import renpy.store as store
import copy


class MERCore(object):

    def __init__(self):

        self._player = None
        self._world = 'core'
        self._journal = EventsBook(0)
        self._wish_maker = WishesGenerator()
        self.person_creator = PersonCreator()

    def _get_active_persons(self):
        return self.faction.get_members()

    def process_wishes(self):
        for i in self._get_active_persons():
            i.wishes_turn_end()
            self._wish_maker.make_wishes(i)

    def process_bonds(self):
        for i in self._get_active_persons():
            bonds = i.get_bonds()
            for n in range(0, i.occupation_level) and len(bonds) > 0:
                bond = random.choice(bonds)
                bonds.remove(bond)
                bond.target.resources_bonus += 1

    def process_resources(self):
        for person in self._get_active_persons():
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

    @property
    def player(self):
        return self._player

    def set_player(self, person):
        self._player = person
        person.player_controlled = True

    @property
    def world(self):
        return self._world

    def skip_turn(self):
        self._journal.skip_turn()
        self.process_wishes()
        self._player.rest()
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
            'accommodation': store.basic_accommodations,
            'ration': store.basic_rations,
            'optional': store.basic_extras}
        for key, data in basic_schedule.items():
            for i in data:
                if key == 'job':
                    person.schedule.unlock(key, ScheduleJob(i, data))
                else:
                    person.schedule.unlock(key, ScheduleJob(i, data))


class EventsBook(object):

    def __init__(self, turns_to_store=1):
        self._events = list()
        self._turns_to_store = turns_to_store
        self._turns_passed = 0

    def skip_turn(self):
        self._turns_passed += 1
        if self._turns_passed > self._turns_to_store:
            self._events = list()
            self._turns_passed = 0

    def add_entry(self, value):
        self._events.append(value)

    def get_records(self):
        return copy.copy(self._events)
