init python:

    basic_jobs = {
        'idle': 
            {
                'name': __('Idle'), 
                'description': 'Idle\nTimid deed. Just rest and take your time for yourself. Gain enregy.', 
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
            'description': __("Rent a flatlet. 25 bars/decade"), 
            'cost': 25, 
            'world': None
            },
    }
    basic_rations = {
        'cooked': 
            {
            "name": __("Cooked food"), 
            'description': __("Eat cooked food in a pub. Don't ask wich meat it is. 20 bars/decade"), 
            'cost': 20, 
            'world': None
            },
    }