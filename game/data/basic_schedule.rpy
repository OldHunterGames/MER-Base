init python:

    basic_jobs = {
        'idle': 
            {
                'name': __('Idle'), 
                'description': 'Idle\nJust rest and take your time for yourself.\n(Timid deed. Well rested - gain green action card.  Stagnation tenses your ambitions)', 
                'skill': None, 
                'difficulty': 0, 
                'world': None, 
                'image': 'miscards', 
            },
    }
    basic_accommodations = {
        'appartment': 
            {
            "name": __("Appartments"), 
            'description': __("Standart apartments. 25 sparks/decade"), 
            'cost': 25, 
            'world': 'core'
            },
        'unsheltered':
            {
                "name": __("Unsheltered"),
                "description": __(""),
                'cost': 0,
                'world': 'core'
            },
        'camping': 
            {
            "name": __("Camping"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'confined': 
            {
            "name": __("Confined"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'cold_floor': 
            {
            "name": __("Cold floor"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'cot_and_blanket': 
            {
            "name": __("Cot & Blanket"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'comfortable_bed': 
            {
            "name": __("Comfortable bed"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'private_bedroom': 
            {
            "name": __("Private bedroom"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'love_nest': 
            {
            "name": __("Love nest"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
    }
    basic_rations = {
        'cooked': 
            {
            "name": __("Cooked food"), 
            'description': __("Eat cooked food in a pub. 20 sparks/decade"), 
            'cost': 20, 
            'world': 'core'
            },
    }

label core_ration_cooked(person):
    $ person.satisfy_need('nutrition', 'point', 3)
    # '[person.name] eats coocked food'
    return

label core_accommodation_appartment(person):
    $ person.satisfy_need('comfort', 'point', 3)
    # '[person.name] sleeps in good appartments'
    return

label none_job_idle(person):
    # '[person.name] do no job at all'
    return

label core_accommodation_unsheltered(person):
    return

label core_accommodation_camping(person):
    return

label core_accommodation_confined(person):
    return

label core_accommodation_cold_floor(person):
    return

label core_accommodation_cot_and_blanket(person):
    return

label core_accommodation_comfortable_bed(person):
    return

label core_accommodation_private_bedroom(person):
    return

label core_accommodation_love_nest(person):
    return