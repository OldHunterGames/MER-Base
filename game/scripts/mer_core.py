# -*- coding: UTF-8 -*-


class MERCore(object):

    def __init__(self):

        self._player = None
        self._world = None

    def set_player(self, person):
        self._player = person
        person.player_controlled = True

    @property
    def world(self):
        return self._world
