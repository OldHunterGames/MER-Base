init python:
    wishes_data = {
        'wealth': {
            'name': __('Wealth'),

        }
    }

label lbl_wish_wealth_end(person):
    '[person.name] fulfilled wealth wish'
    return

label lbl_wish_wealth_chance(person):
    return 5 - person.resource('cash') + person.need_level('prosperity')

label lbl_wish_wealth_turn_end(person):
    $ core.add_record("{person.name} gains +1 cash".format(person=person))
    $ person.add_resource('cash', 1)
    return

label lbl_wish_wealth_fulfill(person):
    return person.has_resource('cash', 5)