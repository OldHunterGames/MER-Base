init python:

    class PickConditionCard(Card, Command):

        def __init__(self, person, condition):

            self.person = person
            self.condition = condition

        def image(self):
            return self.condition.image()

        def name(self):
            return self.condition.name()

        def description(self):
            return self.condition.description()

        def run(self):
            self.person.add_condition(self.condition)


label lbl_pick_condition(person, conditions):
    python:
        cards = [PickConditionCard(person, i) for i in conditions]
        CardMenu(cards).show()
    return

label test_pick_any_condition(person):
    python:
        conditions = [core.conditions_maker.make_condition(
            i, 1) for i in store.conditions_data.keys()]
        cards = [PickConditionCard(person, i) for i in conditions]
        CardMenu(cards).show()
    return