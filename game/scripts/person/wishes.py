import renpy.store as store
import renpy.exports as renpy
from mer_utilities import weighted_random


class Wish(object):
    "Wish object simply wraps renpy dict and labels"

    def __init__(self, id_):

        self.id = id_

    def name(self):
        return self.data.get('name', "No name")

    def description(self):
        return self.data.get('description', 'No description')

    def _get_label(self, name):
        return 'lbl_wish_%s_%s' % (self.id, name)

    def _end_label(self):
        return self._get_label('end')

    def _chance_label(self):
        return self._get_label('chance')

    @property
    def data(self):
        return store.wishes_data.get(self.id)

    def activate(self, person):
        # called when whish is fulfilled
        renpy.call_in_new_context(self._end_label(), person=person)

    def appearance_chance(self, person):
        # gets chance for wish to appear at this person
        chance = renpy.call_in_new_context(self._chance_label(), person=person)
        return max(0, chance)


class WishesGenerator(object):

    def __init__(self, max_wishes=1):
        self.max_wishes = max_wishes
        self._reserved_wishes = dict()

    def reserve_wish(self, person, wish_id):
        self._reserved_wishes[person] = wish_id

    def _get_wishes(self):
        return store.wishes_data.keys()

    def process_wishes(self, person):
        reserved = self._reserved_wishes.get(person)
        if reserved is not None:
            Wish(reserved).activate(person)
            del self._reserved_wishes[person]
            return
        available_wishes = [Wish(i) for i in self._get_wishes()]
        pairs = {}
        for i in available_wishes:
            chance = i.appearance_chance(person)
            if chance > 0:
                pairs[i] = chance
        wish = weighted_random(pairs)
        wish.activate(person)
