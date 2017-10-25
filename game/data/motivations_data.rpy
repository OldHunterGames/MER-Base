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

    def wrap_desperation(motivation, person):
        def desperation_skillcheck_callback(skillcheck, *args):
            if skillcheck.person == person:
                skillcheck.remove_callback(desperation_skillcheck_callback)
                person.remove_motivation(motivation)
        return desperation_skillcheck_callback

label lbl_motivation_desperation_run(motivation, person):
    $ Skillcheck.run.add_callback(wrap_desperation(motivation, person))
    $ conditions = core.conditions_maker.make_conditions('angst', 1)
    call lbl_pick_condition(person, conditions)
    return
