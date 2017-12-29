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
        'taste': __("Taste"),
        'hunger': __("Hunger"),
        'confidence': __("Confidence"),
        'fear': __("Fear"),
        'pleasure': __("Pleasure"),
        'pain': __("Pain"),
        'adrenaline': __("Adrenaline"),
        'deprivation': __("Deprivation"),
        'satisfaction': __("Satisfaction"),
        'desire': __("Desire"),
        'attention': __("Attention"),
        'neglect': __("Neglect"),
        'rapture': __("Rapture"),
        'gloom': __("Gloom"),
        'opulence': __("Opulence"),
        'misery': __("Misery"),
        'humiliation': __("Humiliation"),
        'supremacy': __("Supremacy"),
        'achievement': __("Achievement"),
        'incompetence': __("Incompetence"),
    }

label lbl_motivation_desperation_run(motivation, person):
    $ conditions = core.conditions_maker.make_conditions('angst', 1)
    call lbl_pick_condition(person, conditions)
    return
