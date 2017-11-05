screen sc_pick_house(person):
    python:
        house = core.dweller_house(person)
        if house is not None:
            house_id = house.id
        else:
            house_id = None
        houses = [core.get_house(i) for i in housing_data.keys() if i != house_id]

    window:
        style 'char_info_window'
        vbox:
            for i in houses:
                textbutton i.name():
                    action Function(core.add_dweller, person, i)

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