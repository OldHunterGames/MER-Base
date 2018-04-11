# -*- coding: UTF-8 -*-
import renpy.exports as renpy
from mer_command import Command, Card, CardMenu


class InteractionCard(Command, Card):

    def __init__(self, interaction, source, actor):
        self.interaction = interaction
        self._source = source
        self._actor = actor

    def run(self):
        return self.interaction.interact(self._source, self._actor)

    def description(self):
        return self.interaction.description()

    def name(self):
        return self.interaction.name()


class InteractionsMenu(CardMenu):

    def __init__(self, source, actor, *args, **kwargs):
        ability = source.ability
        print(ability.interactions())
        interactions = []
        if ability is not None:
            for i in ability.interactions():
                interaction = Interaction.get_interaction(i)
                interactions.append(InteractionCard(interaction, source, actor))
        interactions.extend(source.get_interactions())
        print(interactions)
        super(InteractionsMenu, self).__init__(interactions, cancel=True, *args, **kwargs)


class Interaction(object):

    INTERACTIONS = dict()

    @staticmethod
    def add_interactions(data_dict):
        for key, value in data_dict.items():
            Interaction.INTERACTIONS[key] = Interaction(key, value)

    @staticmethod
    def get_interaction(id):
        return Interaction.INTERACTIONS[id]

    def __init__(self, id, data):

        self._id = id
        self._data = data

    def name(self):
        return self._data.get('name', 'No name')

    def description(self):
        return self._data.get('description', 'No description')

    def interact(self, source, actor):
        lbl = 'lbl_interaction_%s' % self._id
        if renpy.has_label(lbl):
            return renpy.call_in_new_context(lbl, source=source, actor=actor)