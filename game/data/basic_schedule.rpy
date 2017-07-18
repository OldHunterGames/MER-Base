init python:

    basic_jobs = {
        'idle': 
            {
                'name': __('Idle'), 
                'description': 'Idle\nJust rest and take your time for yourself.\n(Timid deed. Well rested - gain green action card.  Stagnation tenses your ambitions)', 
                'skill': None, 
                'difficulty': 0, 
                'world': 'core', 
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

label core_job_idle(person):
    # '[person.name] do no job at all'
    return