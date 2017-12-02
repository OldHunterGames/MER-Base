init python:
    class CardPickHouse(Card, Command):

        def __init__(self, house_card, person, core):
            self.house_card = house_card
            self.person = person
            self.core = core

        def run(self):
            self.core.add_dweller(self.person, self.house_card)

        def image(self):
            return self.house_card.image()

        def name(self):
            return self.house_card.name()

        def description(self):
            return self.house_card.description()

    class CardRemoveHouse(Card, Command):

        def __init__(self, person, core):
            self.person = person
            self.core = core

        def image(self):
            return empty_card()

        def name(self):
            return 'Remove house'

        def description(self):
            return 'Makes person homeless'

        def run(self):
            return self.core.remove_dweller(self.person)

screen sc_pick_house(person):
    python:
        house = core.dweller_house(person)
        if house is not None:
            house_id = house.id
        else:
            house_id = None
        houses = [CardPickHouse(core.get_house(i), person, core) for i in housing_data.keys() if i != house_id]
        if house_id is not None:
            houses.append(CardRemoveHouse(person, core))

    window:
        style 'char_info_window'
        vbox:
            if house is not None:
                imagebutton:
                    idle im.Scale(house.image(), 200, 300)
                    action Function(CardMenu(houses, cancel=True).show)
                text house.name():
                    xalign 0.5
            else:
                imagebutton:
                    idle im.Scale(empty_card(), 200, 300)
                    action Function(CardMenu(houses, cancel=True).show)
                text 'No house':
                    xalign 0.5


        

        vbox:
            xalign 1.0
            text 'Info:'
            if house is not None:
                text "Current house is %s" % (house.name())
                text house.description()
                text 'Resources provided: '
                for key, value in house.resources().items():
                    text "%s: %s" %(key, value)
                text 'Currently used: '
                for key, value in house.used_resources().items():
                    text "%s: %s" %(key, value)
                text 'Resource overuse: '
                for key, value in house.resource_overuse().items():
                    text "%s: %s" %(key, value)
                if not house.has_resources():
                    text encolor_text("You can't skip turn", 'red')
            else:
                text '[person.name] currently has no house'
        if house is not None:
            if house.type() == 'house':
                vbox:
                    xalign 0.5
                    for i in house.available_premises():
                        python:
                            txt = i.type
                            if i.premise is not None:
                                txt += ': %s' % i.premise.name()
                        textbutton txt action Show('sc_pick_premise', premise=i)

        textbutton 'Leave':
            yalign 1.0
            action Hide('sc_pick_house')


screen sc_pick_premise(premise):
    python:
        if premise.premise is not None:
            premise_id = premise.premise.id
            try:
                inner_premises = [i for i in premise.premise.available_premises()]
            except AttributeError:
                inner_premises = []
        else:
            premise_id = None
            inner_premises = []
        premises = [i for i in core._housing.available_premises(premise.type) if i.id != premise_id]
    modal True
    window:
        style 'char_info_window'
        vbox:
            text 'Premises of type: %s' % premise.type
            for i in premises:
                textbutton i.name():
                    action Function(premise.set_premise, i), Hide('sc_pick_premise')
            textbutton "remove premise":
                action Function(premise.set_premise, None), Hide('sc_pick_premise')

            textbutton "Leave" action Hide('sc_pick_premise')

        if inner_premises:
            vbox:
                xalign 0.5
                for i in inner_premises:
                    python:
                        txt = i.type
                        if i.premise is not None:
                            txt += ': %s' % i.premise.name()
                    textbutton txt action Show('sc_pick_premise', premise=i)