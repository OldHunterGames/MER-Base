# -*- coding: UTF-8 -*-
from mer_person import PersonCreator
from schedule import ScheduleObject
import renpy.exports as renpy
import renpy.store as store
import copy


class MERCore(object):

    def __init__(self):

        self._player = None
        self._world = 'core'
        self._journal = EventsBook()

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
        self._player.rest()
        renpy.call_in_new_context('lbl_turn_end')

    def can_skip_turn(self):
        return self._player.can_tick()

    def create_player(self):
        player = PersonCreator().gen_random_person()
        self.set_player(player)
        player.civil_income = 100

    def unlock_optionals(self, person):
        for i in store.basic_extras:
            person.schedule.unlock(
                'optional', ScheduleObject(i, store.basic_extras))


class EventsBook(object):

    def __init__(self, turns_to_store=1):
        self._events = list()
        self._turns_to_store = 1
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
