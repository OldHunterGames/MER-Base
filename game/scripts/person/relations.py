# -*- coding: UTF-8 -*-
from copy import copy
from collections import OrderedDict

import renpy.store as store
import renpy.exports as renpy

from mer_utilities import encolor_text


class Relations(object):
    """Represents relations between persons"""
    _authority_alignment = 'activity'
    _distance_alignment = 'orderliness'
    _affection_alignment = 'morality'

    DOMINANT = 'dominant'
    SUBMISSIVE = 'submissive'
    FORMAL = 'formal'
    PERSONAL = 'personal'
    SUPPORTER = 'supporter'
    HATER = 'hater'

    _sides_alignments = {
        DOMINANT: 'ardent',
        SUBMISSIVE: 'timid',
        FORMAL: 'lawful',
        PERSONAL: 'chaotic',
        SUPPORTER: 'good',
        HATER: 'evil'
    }

    def __init__(self, target):
        self._target = target
        self._sides = {'authority': None, 'distance': None, 'affection': None}
        self._influence = 0
        self._soulmate = False
        self._special_stance = None

    @property
    def influence(self):
        return self._influence

    @influence.setter
    def influence(self, value):
        self._influence = max(0, min(5, value))

    @property
    def target(self):
        return self._target

    def make_soulmate(self, special_stance):
        self._special_stance = special_stance
        self._soulmate = True

    @property
    def soulmate(self):
        return self._soulmate

    def stance(self, protected=False):
        if self._special_stance is not None:
            stance = store.special_stances[self._special_stance]
        else:
            key = (
                self._sides['authority'],
                self._sides['distance'],
                self._sides['affection'])
            stance = store.stances[key]

        harmony = self.harmony()
        if harmony == 0:
            color = 'cyan'
        elif harmony > 0:
            color = 'green'
        elif harmony < 0:
            color = 'red'
        if self._soulmate:
            color = 'gold'
        return encolor_text(stance, color, protected)

    @property
    def authority(self):
        return self._sides['authority']

    def set_authority(self, value):
        self._sides['authority'] = value

    @property
    def distance(self):
        return self._sides['distance']

    def set_distance(self, value):
        self._sides['distance'] = value

    @property
    def affection(self):
        return self._sides['affection']

    def set_affection(self, value):
        self._sides['affection'] = value

    def antagonism(self):
        return self._compare_alignment(self._antagonism)

    def comprehension(self):
        return self._compare_alignment(self._comprehension)

    def resonance(self):
        return self._compare_alignment(self._resonance)

    def harmony(self):
        # affects amount of events, relations checks and favor/respect
        # consumption
        return self.comprehension() + 2 * self.resonance() - self.antagonism()

    def show_sides(self, protected=False):
        sides = []
        for i in self._sides.keys():
            side_alignment = self._target.feature_by_slot(
                getattr(self, '_%s_alignment' % i))
            side_alignment = side_alignment and side_alignment.id
            side = self._sides[i]
            if self._antagonism(side_alignment, side):
                color = 'red'
            elif self._comprehension(side_alignment, side):
                color = 'green'
            elif self._resonance(side_alignment, side):
                color = 'gold'
            if side is not None:
                sides.append(
                    encolor_text(store.relations_sides[side], color, protected))
        return sides

    def bias(self):
        sides = dict()
        for i in self._sides.keys():
            side_alignment = self._target.feature_by_slot(
                getattr(self, '_%s_alignment' % i))
            side_alignment = side_alignment and side_alignment.id
            side = self._sides[i]
            if side_alignment is None:
                if side is not None:
                    sides[i] = side
                else:
                    sides[i] = None
            else:
                sides[i] = self._sides_alignments[side_alignment]
        return sides

    def _compare_alignment(self, check_func):
        value = 0
        for i in self._sides.keys():
            side_alignment = self._target.feature_by_slot(
                getattr(self, '_%s_alignment' % i))
            side_alignment = side_alignment and side_alignment.id
            side = self._sides[i]
            if check_func(side_alignment, side):
                value += 1
        return value

    def _antagonism(self, side_alignment, side):
        if side is None or side_alignment is None:
            return False
        else:
            if self._sides_alignments[side] != side_alignment:
                return True
        return False

    def _comprehension(self, side_alignment, side):
        if side is not None and side_alignment is None:
            return True
        return False

    def _resonance(self, side_alignment, side):
        if side is None:
            return False
        else:
            if self._sides_alignments[side] == side_alignment:
                return True
        return False


class Bond(object):

    def __init__(self, target, id):
        self.id = id
        self._target = target

    @property
    def target(self):
        return self._target

    @property
    def value(self):
        return self._get_data('value', 0)

    def name(self):
        return self._get_data('name', 'No name')

    def description(self):
        return self._get_data('description', 'No description')

    def _get_data(self, key, value=None):
        return store.bonds_data[self.id].get(key, value)
