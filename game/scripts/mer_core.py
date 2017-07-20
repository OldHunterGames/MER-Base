# -*- coding: UTF-8 -*-
from mer_person import PersonCreator
import renpy.exports as renpy


class MERCore(object):

    def __init__(self):

        self._player = None
        self._world = 'core'

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
        self._player.rest()
        renpy.call_in_new_context('lbl_turn_end')

    def can_skip_turn(self):
        return self._player.can_tick()

    def create_player(self):
        player = PersonCreator().gen_random_person()
        self.set_player(player)
        player.civil_income = 100
