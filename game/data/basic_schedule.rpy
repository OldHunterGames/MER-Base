init python:

    basic_jobs = {
        'idle': 
            {
                'name': __('Idle'), 
                'description': 'Idle\nTimid deed. Just rest and take your time for yourself. Gain enregy.', 
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
            'description': __("Rent a flatlet. 25 bars/decade"), 
            'cost': 25, 
            'world': 'core'
            },
    }
    basic_rations = {
        'cooked': 
            {
            "name": __("Cooked food"), 
            'description': __("Eat cooked food in a pub. Don't ask wich meat it is. 20 bars/decade"), 
            'cost': 20, 
            'world': 'core'
            },
    }

label core_ration_cooked(person):
    $ person.satisfy_need('nutrition', 'point', 3)
    '[person.name] eats coocked food'
    return

label core_accommodation_appartment(person):
    $ person.satisfy_need('comfort', 'point', 3)
    '[person.name] sleeps in good appartments'
    return

label core_job_idle(person):
    '[person.name] do no job at all'
    return