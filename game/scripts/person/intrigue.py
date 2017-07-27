import renpy.store as store
import renpy.exports as renpy


class Intrigue(object):

    def __init__(self, id, initiator, target, player):
        self.id = id
        self.initiator = initiator
        self.target = target
        self.player = player

    def apply(self):
        self._on_init()
        self.initiator.die.add_callback(self._die_callback)
        self.target.die.add_callback(self._die_callback)

    def data(self):
        return store.intrigues_data[self.id]

    @property
    def name(self):
        return self.data().get('name', 'No name')

    def _end_label(self):
        return 'lbl_intrigue_%s_end' % self.id

    def _check_label(self):
        return 'lbl_intrigue_%s_check' % self.id

    def _intervene_label(self):
        return 'lbl_intrigue_%s_intervene' % self.id

    def _on_init(self):
        lbl = 'lbl_intrigue_%s_on_init' % self.id
        try:
            return renpy.call_in_new_context(lbl, self)
        except:
            return

    def is_available(self):
        try:
            return renpy.call_in_new_context(self._check_label(), self)
        except:
            return True

    def end(self):
        try:
            renpy.call_in_new_context(self._end_label(), self)
        except:
            raise Exception('intrigue %s has no end label' % self.id)
        finally:
            self.initiator.die.remove_callback(self._die_callback)
            self.target.die.remove_callback(self._die_callback)

    def intervene(self):
        try:
            renpy.call_in_new_context(self._intervene_label(), self)
        except:
            raise Exception("intrigue '%s' has no intervene label" % self.id)

    def can_intervene(self):
        return renpy.has_label(self._intervene_label())

    def _die_callback(self, *args, **kwargs):
        self.initiator.remove_intrigue()
        self.initiator.die.remove_callback(self._die_callback)
        self.target.die.remove_callback(self._die_callback)
