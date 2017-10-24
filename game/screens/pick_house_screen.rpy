screen sc_pick_house(person):
    python:
        house = core.dweller_house(person)
        if house is not None:
            house_id = house.id
        else:
            house_id = None
        houses = [core.get_house(i) for i in housing_data.keys() if i != house_id]
        print houses

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
            else:
                text '[person.name] currently has no house'

        textbutton 'Leave':
            yalign 1.0
            action Hide('sc_pick_house')