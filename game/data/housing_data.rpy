init python:
    housing_data = {
        'pod_hotel': {
            'name': __("Pod hotel"),
            'description': __("Pod hotel"),
            'house_type': 'Hostel',
            'cost': 10
        },
        'inn': {
            'name': __('Inn'),
            'description': __("Inn"),
            'house_type': 'Hostel',
            'cost': 25,
            'schedule_options': [('cold_floor', 'basic_accommodations')]
        },

        'house': {
            'name': __("House"),
            'description': __("House"),
            'house_type': 'PremisedHousing',
            'type': 'house',
            'available_premises': ['cell']
        },

        
    }

    housing_updates = {
        'empty_cell': {
            'name': __("Empty cell"),
            "description": __("Empty cell"),
            'house_type': "Premise",
            'upkeep': 1,
            'schedule_options': [('cold_floor', 'basic_accommodations')],
            'resources': {'freespace': 1},
            'type': 'cell',
        }
    }