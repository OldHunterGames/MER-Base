# -*- coding: <UTF-8> -*-

import renpy.store as store
import renpy.exports as renpy
import mer_utilities


needs_names = ["nutrition", "wellness", "comfort", "activity", "communication",
               "amusement", "prosperity", "authority", "ambition", "eros"]

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
    for name in needs_names:
        dict_[name] = (Need(name))
    return dict_


class Motivation(object):
    _types_colors = {
        'desperation': 0, 'stress': 2, 'determination': 4, 'enthusiasm': 5}

    def __init__(self, id_, type_):
        self.id = id
        self.type = type

    def name(self):
        return mer_utilities.encolor_text(
            store.motivations_dict[self.id],
            self._types_colors[self.type])

    def image(self):
        return


class Need(object):
    def __init__(self, name):
        self.name = name
        self.tokens = []
        self.tension_points = []
        self.satisfaction_points = []
        self._saturation = 0
        self.satisfied = False

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
        if value <= self.saturation or self.satisfied:
            return
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
        return point in self.tension_point

    def has_satisfaction(self, point):
        return point in self.satisfaction_points

    def remove_tension(self, point):
        self.tension_points.remove(point)

    def tensed(self):
        return len(self.tension_points) > 0

    def reset(self, reset_satisfactions=True):
        if reset_satisfactions:
            self.satiscation_points = []
        self.tension_points = []
        self.saturation -= 1
        if self.saturation <= 0:
            self.satisfied = False


class PsyModel(object):

    def init_psymodel(self):

        self._motivations = []
        self._chances = {}
        self.needs = init_needs()
        self.inactive_needs = []
        self.check_bonus = 0

    def deactivate_need(self, id):
        self.inactive_needs.append(id)

    def activate_need(self, id):
        self.inactive_needs.remove(id)

    def add_motivation(self, motivation):
        if not self.has_motivation(motivation):
            self._motivations.append(motivation)

    def remove_motivation(self, id):
        for i in self._motivations:
            if i.id == id:
                self._motivations.remover(i)
                return

    def has_motivation(self, motivation):
        return motivation.id in [i.id for i in self._motivations]

    def has_enthusiasm(self):
        return any(self.get_enthusiasm())

    def get_enthusiasm(self):
        return [i for i in self._motivations if i.type == 'enthusiasm']

    def get_motivations(self):
        return [i for i in self._motivations]

    def use_motivation(self, motivation):
        self._motivations.remove(motivation)
        self.check_bonus += self.run_motivation(motivation)

    def run_motivation(self, motivation):
        if motivation.type == 'desperation':
            # adds 1 random angst condition
            # self.add_condition()
            return -1
        elif self.type == 'stress':
            # chose 1 angst condition
            return 0
        elif self.type == 'determination':
            return 0
        else:
            return 1

    def moral_action(self, **kwargs):
        # checks moral like person.check_moral, but instantly affect selfesteem
        result = self.check_moral(**kwargs)
        return result

    def check_moral(self, **kwargs):
        act = {'ardent': 1, 'reasonable': None, 'timid': -1}
        moral = {'good': 1, 'selfish': None, 'evil': -1}
        order = {'lawful': 1, 'conformal': None, 'chaotic': -1}
        target = kwargs.get('target')
        action_tones = {
            'activity': act.get(kwargs.get('activity')),
            'morality': moral.get(kwargs.get('morality')),
            'orderliness': order.get(kwargs.get('orderliness'))
        }
        relation_tones = {}
        if target is not None:
            for key in action_tones.keys():
                relation_tones[key] = getattr(
                    self.relations(target), self.alignment.relation_binding[key])
        else:
            for key in action_tones.keys():
                relation_tones[key] = 0

        for key, value in action_tones.items():
            if value is not None:
                valself = getattr(self.alignment, key)
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

                    if valself == 0:
                        if tone + valact == 0:
                            chance_value = 2
                            result = 'bad'
                        elif abs(tone + valact) == 2:
                            chance_value = 4
                            result = 'good'
                    elif valself == tone:
                        if valact + tone == 0:
                            chance_value = 5
                            result = 'good'
                    elif valself != tone:
                        if abs(valact + tone) == 2:
                            chance_value = 3
                            result = 'bad'

    def get_need(self, name):
        return self.needs[name]

    def need_level(self, name):
        return max(-1, min(1, self.count_modifiers(name)))

    def tense_need(self, name, point):
        if name in self.inactive_needs:
            return
        need_obj = self.needs[name]
        need_obj.set_tension(point)

    def satisfy_need(self, name, point, value):
        if name in self.inactive_needs:
            return
        need_obj = self.needs[name]
        need_obj.set_satisfaction(point, value)

    def reset_psych(self):
        self._motivations = []
        for need in self.needs.values():
            if need.id in self.inactive_needs:
                continue
            if need.saturation < 0:
                need.set_tension(needs_default_points[need.id])
            level = self.need_level(need.id)
            if level == 1:
                for i in need.satisfaction_points:
                    self.add_motivation(Motivation(i, 'enthusiasm'))
                for i in need.tension_points:
                    self.add_motivation(Motivation(i, 'desperation'))
            elif level == 0:
                for i in need.satisfaction_points:
                    self.add_motivation(Motivation(i, 'determination'))
                for i in need.tension_points:
                    self.add_motivation(Motivation(i, 'stress'))