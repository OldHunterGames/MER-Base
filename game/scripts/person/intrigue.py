import renpy.store as store
import renpy.exports as renpy


class Intrigue(object):

    def __init__(self, id, initiator, target, player):
        self.id = id
        self.initiator = initiator
        self.target = target
        self.player = player
        self.player_influence = False
        if self.is_available():
            self._on_init()
            initiator.set_intrigue(self)

    def data(self):
        return store.intrigues_data[self.id]

    @property
    def name(self):
        return self.data().get('name', 'No name')

    def _end_label(self):
        return self.data().get('end_label')

    def _check_label(self):
        return self.data().get('check_label')

    def _on_init(self):
        return renpy.call_in_new_context(
            self.data().get('on_init_label'), self)

    def is_available(self):
        return renpy.call_in_new_context(self._check_label(), self)

    def end(self):
        renpy.call_in_new_context(self._end_label(), self)
