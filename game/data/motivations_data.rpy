init python:
    motivations_data = {
        'desperation': {
            'name': __("Desperation"),
            'type': 'desperation'
        },
        
        'stress': {
            'name': __("Stress"),
            'type': 'stress'
        },
        
        'determination': {
            'name': __("Determination"),
            'type': 'determination'
        },
        
        'enthusiasm': {
            'name': __("Enthusiasm"),
            'type': 'enthusiasm'
        }
    }

    motivations_keys = {
        'key': __("Key"),

    }

label lbl_motivation_desperation_run(motivation, person):
    $ conditions = core.conditions_maker.make_conditions('angst', 1)
    call lbl_pick_condition(person, conditions)
    return
