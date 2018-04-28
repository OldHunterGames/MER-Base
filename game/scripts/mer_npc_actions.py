# -*- coding: <UTF-8> -*-
import renpy.exports as renpy
from collections import defaultdict
from mer_command import NpcActionCommand
from mer_utilities import weighted_random


class CoreNpcAction(object):

    ACTIONS = dict()

    def __init__(self, id, data, *args, **kwargs):
        self._id = id
        self._data = data
        self._data.get('on_init', lambda x: x)(self)

    def name(self):
        return self._data.get('name', 'No name')

    def description(self):
        return self._data.get("description", 'No description')

    def chance(self, person):
        lbl = 'lbl_npc_action_%s_chance' % self._id
        if renpy.has_label(lbl):
            return renpy.call_in_new_context(lbl, person=person, action=self)
        return 0

    def act(self, person):
        lbl = 'lbl_npc_action_%s_act' % self._id
        if renpy.has_label(lbl):
            return renpy.call_in_new_context(lbl, person=person, action=self)

    @staticmethod
    def add_action(action_id, data):
        cls = data.get('cls')
        if cls is None:
            CoreNpcAction.ACTIONS[action_id] = CoreNpcAction(action_id, data)
        else:
            CoreNpcAction.ACTIONS[action_id] = cls(action_id, data)

    @staticmethod
    def get_action(id):
        return CoreNpcAction.ACTIONS[id]

    @staticmethod
    def randomize_action(person):
        weights = {}
        for action in CoreNpcAction.ACTIONS.values():
            weights[action] = action.chance(person)
        action = weighted_random(weights)
        NpcActionCommand(person, action).run()


class VacationAction(CoreNpcAction):

    def __init__(self, *args, **kwargs):
        super(VacationAction, self).__init__(*args, **kwargs)
        self.action_fatigue = defaultdict(int)
        NpcActionCommand.run.add_callback(self._on_another_action_callback)
    
    def _on_another_action_callback(self, command, *args, **kwargs):
        if command.action == self:
            self.action_fatigue[command.npc] -= 1
        else:
            self.action_fatigue[command.npc] += 1
        if self.action_fatigue[command.npc] < 0:
            self.action_fatigue[command.npc] = 0
