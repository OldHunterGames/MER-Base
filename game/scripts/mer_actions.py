# -*- coding: <UTF-8> -*-

from collections import defaultdict
import renpy.store as store
import renpy.exports as renpy
from mer_command import Card, Command
from mer_utilities import empty_card


class Action(object):


    class ActionCard(Card, Command):

        source = 'action'

        def __init__(self, action, person):
            self.action = action
            self.person = person

        def run(self):
            return renpy.call_in_new_context(self.action.lbl(), action=self)

        def image(self):
            return empty_card()

    def __init__(self, id, name, description, lbl):
        self._id = id
        self._name = name
        self._description = description
        self._lbl = lbl
    
    def lbl(self):
        return self._lbl

    def name(self):
        return self._name

    def description(self):
        return self._description
    
    def produce_card(self, person):
        return self.ActionCard(self, person)


class Actions(object):
    _registered_actions = {}

    def __init__(self):
        self._persons_actions = defaultdict(set)


    @staticmethod
    def register_actions(dict_):
        for key, value in dict_.items():
            Actions._registered_actions[key] = Action(key, value['name'], value['description'], value['lbl'])

    def unlock_action(self, person, action_id):
        if action_id not in self._registered_actions.keys():
            raise Exception('unregistered action %s' % action_id)
        self._persons_actions[person].add(action_id)

    def remove_action(self, person, action_id):
        if action_id not in self._registered_actions.keys():
            raise Exception('unregistered action %s' % action_id)
        try:
            self._persons_actions[person].remove(action_id)
        except KeyError:
            pass

    def get_actions_for(self, person):
        return [value.produce_card(person) for key, value in self._registered_actions.items() if key in self._persons_actions[person]]