# -*- coding: <UTF-8> -*-

import renpy.store as store
import renpy.exports as renpy
import mer_utilities as utilities
import copy
from motivation import Motivation


satisfy_chances = {
    'nutrition': 'taste',
    'wellness': 'health',
    'comfort': 'bliss',
    'activity': 'adrenaline',
    'eros': 'orgasm',
    'communication': 'intimacy',
    'amusement': 'entertainment',
    'prosperity': 'gain',
    'authority': 'respect',
    'ambition': 'accomplishment'
}
needs_default_points = {}


def init_needs():
    dict_ = {}
    for id, name in store.needs_names.items():
        dict_[id] = (Need(id, name))
    return dict_


class Need(object):
    def __init__(self, id, name):
        self.name = name
        self.tokens = []
        self.tension_points = []
        self.satisfaction_points = []
        self._saturation = 0
        self.satisfied = False
        self.id = id

    @property
    def saturation(self):
        return self._saturation

    @saturation.setter
    def saturation(self, value):
        self._saturation = value

    def use_token(self, token):
        self.tokens.append(token)

    def token_used(self, token):
        return token in self.tokens

    def set_satisfaction(self, point, value):
        if self.has_satisfaction(point):
            return
        if value <= self.saturation:
            return
        print point.encode('utf-8')
        print 'saturation: {0} | value: {1}'.format(self.saturation, value)
        self.satisfaction_points.append(point)
        self.saturation = 5
        self.satisfied = True

    def set_tension(self, point):
        if self.has_tension(point):
            return
        self.tension_points.append(point)
        if self.saturation > 0:
            self.saturation -= 1

    def has_tension(self, point):
        return point in self.tension_points

    def has_satisfaction(self, point):
        return point in self.satisfaction_points

    def remove_tension(self, point):
        self.tension_points.remove(point)

    def tensed(self):
        return len(self.tension_points) > 0

    def reset(self, reset_satisfactions=True):
        if reset_satisfactions:
            self.satisfaction_points = []
        self.tension_points = []
        self.saturation -= 1
        if self.saturation <= 0:
            self.satisfied = False


class PsyModel(object):

    def init_psymodel(self):

        self._endturn_motivations = []
        self._motivations = []
        self._used_motivations = []
        self._last_used_motivation = None
        self._chances = {}
        self.needs = init_needs()
        self.inactive_needs = []
        self.check_bonus = 0

    def add_motivation(self, card):
        motivations = self.get_motivations()
        motivations.extend(self._used_motivations)
        if card.key in map(lambda x: x.key, motivations):
            return
        self._motivations.append(card)

    def clear_used_motivations(self):
        self._used_motivations = []

    def use_motivation(self, card):
        card.run(self)
        self._used_motivations.append(card)
        self._motivations.remove(card)
        self._last_used_motivation = card

    def used_motivations(self):
        return copy.copy(self._used_motivations)

    def last_used_motivation(self):
        return self._last_used_motivation

    def remove_motivation(self, card):
        self._used_motivations.remove(card)

    def get_motivations(self):
        return copy.copy(self._motivations)

    def has_motivation(self):
        return len(self._motivations) > 0

    def affected_by_enthusiasm(self):
        return any([i.type() == 'enthusiasm' for i in self._used_motivations])

    def deactivate_need(self, id):
        self.inactive_needs.append(id)

    def activate_need(self, id):
        self.inactive_needs.remove(id)

    def moral_action(self, **kwargs):
        # checks moral like person.check_moral, but instantly affect selfesteem
        result = self.check_moral(**kwargs)
        return result

    def check_moral(self, **kwargs):
        activity = {'ardent': 1, 'reasonable': None, 'timid': -1}
        morality = {'good': 1, 'selfish': None, 'evil': -1}
        orderliness = {'lawful': 1, 'conformal': None, 'chaotic': -1}
        target = kwargs.get('target')
        keys = {
            'ardent': {
                'good': 'valor',
                'bad': 'bile'
            },
            'timid': {
                'good': 'serenity',
                'bad': 'apathy'
            },
            'lawful': {
                'good': 'honor',
                'bad': 'rigidity'
            },
            'chaotic': {
                'good': 'independence',
                'bad': 'infidelity'
            },
            'good': {
                'good': 'kindness',
                'bad': 'infirmity'
            },
            'evil': {
                'good': 'power',
                'bad': 'tyranny'
            }
        }
        action_tones = {
            'activity': activity.get(kwargs.get('activity')),
            'morality': morality.get(kwargs.get('morality')),
            'orderliness': orderliness.get(kwargs.get('orderliness'))
        }
        relations_binding = {
            'activity': 'authority',
            'morality': 'affection', 
            'orderliness': 'distance'
        }
        relations_values = {
            'dominant': 1,
            'submissive': -1,
            'formal': 1,
            'personal': -1,
            'supporter': 1,
            'hater': -1
        }
        relation_tones = {}
        if target is not None:
            for key in action_tones.keys():
                relation_tones[key] = relations_values.get(getattr(
                    self.relations(target), relations_binding[key]), 0)
        else:
            for key in action_tones.keys():
                relation_tones[key] = 0

        for key, value in action_tones.items():
            if value is not None:
                valself = getattr(self, key)()
                if valself is None:
                    valself = 0
                else:
                    valself = locals()[key][valself.id]
                valact = value
                result = None
                if target is not None:
                    fake_value = valact
                else:
                    fake_value = None
                tone = relation_tones[key]

                if tone == 0:
                    if valself + valact == 0:
                        chance_value = 1
                        result = 'bad'
                    elif abs(valself + valact) == 2:
                        chance_value = 3
                        result = 'good'
                    else:
                        result = 'neutral'
                else:

                    if valself == 0:
                        if tone + valact == 0:
                            chance_value = 2
                            result = 'bad'
                        elif abs(tone + valact) == 2:
                            chance_value = 4
                            result = 'good'
                        else:
                            result = 'neutral'
                    elif valself == tone:
                        if valact + tone == 0:
                            chance_value = 5
                            result = 'good'
                        else:
                            result = 'neutral'
                    elif valself != tone:
                        if abs(valact + tone) == 2:
                            chance_value = 3
                            result = 'bad'
                        else:
                            result = 'neutral'
            key_name = keys.get(kwargs.get(key))
            if key_name is not None:
                key_name = key_name.get(result)
                if key_name is not None:
                    if result == 'good':
                        self._endturn_motivations.append(Motivation('enthusiasm', key_name))
                    else:
                        self._endturn_motivations.append(Motivation('desperation', key_name))

    def get_need(self, name):
        return self.needs[name]

    def need_level(self, name):
        return max(-1, min(1, self.count_modifiers(name)))

    def tense_need(self, name, point):
        if name in self.inactive_needs:
            return
        need_obj = self.needs[name]
        need_obj.set_tension(point)

    @utilities.Observable
    def satisfy_need(self, name, point, value):
        if name in self.inactive_needs:
            return
        need_obj = self.needs[name]
        need_obj.set_satisfaction(point, value)

    def reset_psych(self):
        self._motivations = []
        self._used_motivations = []
        for i in self._endturn_motivations:
            self.add_motivation(i)
        self._endturn_motivations = []
        for need in self.needs.values():
            if need.id in self.inactive_needs:
                continue
            if need.saturation < 0:
                need.set_tension(store.needs_basic_tension_keys[need.id])
            level = self.need_level(need.id)
            if level == 1:
                for i in need.satisfaction_points:
                    self.add_motivation(Motivation('enthusiasm', i))
                for i in need.tension_points:
                    self.add_motivation(Motivation('desperation', i))
            elif level == 0:
                for i in need.satisfaction_points:
                    self.add_motivation(Motivation('determination', i))
                for i in need.tension_points:
                    self.add_motivation(Motivation('stress', i))
            need.reset()