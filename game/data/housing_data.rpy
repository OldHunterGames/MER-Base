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
            'schedule_options': [('cold_floor', 'basic_accommodations', 5)]
        },

        'house': {
            'name': __("House"),
            'description': __("House"),
            'house_type': 'PremisedHousing',
            'type': 'house',
            'available_premises': {
                'cell': 1,
                'room': 1,
                'hall': 1
            }
        },

        
    }

    housing_updates = {
        'empty_cell': {
            'name': __("Empty cell"),
            "description": __("Upkeep cost 10. This is a small and totally empty room. Gives one free space and for cold floor tiles for sleep."),
            'house_type': "Premise",
            'upkeep': 10,
            'schedule_options': [('cold_floor', 'basic_accommodations', 4)],
            'resources': {'freespace': 1},
            'type': 'cell',
        },
    }
