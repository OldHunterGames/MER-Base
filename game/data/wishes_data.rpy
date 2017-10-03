init python:
    wishes_data = {
        'wealth': {
            'name': __('Wealth'),

        }
    }

label lbl_wish_wealth_end(person):
    '[person.name] fulfilled wealth wish'
    $ core.add_personal_record(person, "{person.name} gains +1 cash".format(person=person))
    $ person.add_resource('cash', 1)
    return

label lbl_wish_wealth_chance(person):
    return 5 - person.resource('cash') + person.need_level('prosperity')
