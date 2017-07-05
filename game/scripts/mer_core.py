# -*- coding: UTF-8 -*-


class MERCore(object):

    def __init__(self):

        self._player = None
        self._world = 'core'

    def set_player(self, person):
        self._player = person
        person.player_controlled = True

    @property
    def world(self):
        return self._world

    def skip_turn(self):
        self._player.rest()

    def can_skip_turn(self):
        return self._player.can_tick()
