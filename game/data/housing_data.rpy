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
        ## CELLS
        'empty_cell': {
            'name': __("Empty cell"),
            "description": __("Reconstruction cost: Free. Upkeep: 10. This is a small and totally empty room. Gives one free space and for cold floor tiles for sleep."),
            'house_type': "Premise",
            'upkeep': 10,
            'reconstruction_cost': 0,
            'schedule_options': [('cold_floor', 'basic_accommodations', 4)],
            'resources': {'freespace': 1},
            'type': 'cell',
        },
        'ward': {
            'name': __("Ward"),
            "description": __(
                "Reconstruction cost: 25. Upkeep 12. This small ward contains torture devices, human size cage and deprivation box for rebellious slaves. Gives one place for incarceration and one for a confinement. Enables advanced torture options."),
            'house_type': "Premise",
            'upkeep': 12,
            'reconstruction_cost': 25,
            'schedule_options': [('confined', 'basic_accommodations', 1)],
            'resources': {'torture': 1},
            'type': 'cell',
        },
        'solo_apartments': {
            'name': __("Solo apartments"),
            "description": __(
                "Reconstruction cost: 50. Upkeep 15. Accommodation for one person, equipped with a bed, a small table, a chair and a wardrobe. Gives one private bedroom and one cold floor tile"),
            'house_type': "Premise",
            'upkeep': 15,
            'reconstruction_cost': 50,
            'schedule_options': [('private_bedroom', 'basic_accommodations', 1), ('cold_floor', 'basic_accommodations', 1)],
            'resources': {},
            'type': 'cell',
        },
        'small_bedroom': {
            'name': __("Small bedroom"),
            "description": __(
                "Reconstruction cost: 50. Upkeep 15. Two comfortable beds, and a bedroom table."),
            'house_type': "Premise",
            'upkeep': 15,
            'reconstruction_cost': 50,
            'schedule_options': [('comfortable_bed', 'basic_accommodations', 2)],
            'resources': {},
            'type': 'cell',
        },
        'small_quarters': {
            'name': __("Small quarters"),
            "description": __(
                "Reconstruction cost: 70. Upkeep 17. Two bunk beds can can accommodate up to four people in this common bedroom"),
            'house_type': "Premise",
            'upkeep': 17,
            'reconstruction_cost': 70,
            'schedule_options': [('cot_and_blanket', 'basic_accommodations', 4)],
            'resources': {},
            'type': 'cell',
        },
        'small_tight_quarters': {
            'name': __("Small tight quarters"),
            "description": __(
                "Reconstruction cost: 80. Upkeep 18. Crude bunks with three tiers allow to accommodate up to six people in a single small cell. The room is so tight and crowded that sleeping here is no better than on a cold floor"),
            'house_type': "Premise",
            'upkeep': 18,
            'reconstruction_cost': 80,
            'schedule_options': [('cold_floor', 'basic_accommodations', 6)],
            'resources': {},
            'type': 'cell',
        },
        'private_study': {
            'name': __("Private study"),
            "description": __(
                "Reconstruction cost: 50. Upkeep 15. It's a nice office place for a one person. Also gives one tile of cold floor to sleep if needed."),
            'house_type': "Premise",
            'upkeep': 15,
            'reconstruction_cost': 50,
            'schedule_options': [('cold_floor', 'basic_accommodations', 1)],
            'resources': {'office': 1},
            'type': 'cell',
        },
        'kitchen': {
            'name': __("Kitchen"),
            "description": __(
                "Reconstruction cost: 100. Upkeep 20. A cook stationed here can feed habitants with a cooked food. There also a one tile of cold floor here."),
            'house_type': "Premise",
            'upkeep': 20,
            'reconstruction_cost': 100,
            'schedule_options': [('cold_floor', 'basic_accommodations', 1)],
            'resources': {'kitchen': 1},
            'type': 'cell',
        },

        ##ROOMS
        'empty_room': {
            'name': __("Empty room"),
            "description": __(
                "Reconstruction cost: Free. Upkeep 18. Empty room gives two free spaces for activities and eight cold floor tiles."),
            'house_type': "Premise",
            'upkeep': 18,
            'reconstruction_cost': 0,
            'schedule_options': [('cold_floor', 'basic_accommodations', 8)],
            'resources': {'freespace': 2},
            'type': 'room',
        },
        'torture_chamber': {
            'name': __("Torture chamber"),
            "description": __(
                "Reconstruction cost: 40. Upkeep 22. This chamber contains torture devices, human size cages and deprivation boxes for rebellious slaves. Gives two places for incarceration and two for a confinement. Enables advanced torture options."),
            'house_type': "Premise",
            'upkeep': 22,
            'reconstruction_cost': 40,
            'schedule_options': [('confined', 'basic_accommodations', 2)],
            'resources': {'torture': 2},
            'type': 'room',
        },
        'common_bedroom': {
            'name': __("Empty room"),
            "description": __(
                "Reconstruction cost: 90. Upkeep 27. Four comfortable beds, pair of chairs and a wardrobe."),
            'house_type': "Premise",
            'upkeep': 27,
            'reconstruction_cost': 90,
            'schedule_options': [('comfortable_bed', 'basic_accommodations', 4)],
            'resources': {},
            'type': 'room',
        },
        'quarters': {
            'name': __("quarters"),
            "description": __(
                "Reconstruction cost: 120. Upkeep 30. Four bunk beds can can accommodate up to eight people in this common bedroom."),
            'house_type': "Premise",
            'upkeep': 30,
            'reconstruction_cost': 120,
            'schedule_options': [('cot_and_blanket', 'basic_accommodations', 8)],
            'resources': {},
            'type': 'room',
        },
        'tight_quarters': {
            'name': __("Tight quarters"),
            "description": __(
                "Reconstruction cost: 130. Upkeep 31. Crude bunks with three tiers allow to accommodate up to 12 people in a single room. This quarters is so tight and crowded that sleeping here is no better than on a cold floor"),
            'house_type': "Premise",
            'upkeep': 31,
            'reconstruction_cost': 130,
            'schedule_options': [('cold_floor', 'basic_accommodations', 12)],
            'resources': {},
            'type': 'room',
        },
        'apartments': {
            'name': __("Apartments"),
            "description": __(
                'Reconstruction cost: 90. Upkeep 27. This apartments is dominated by a wide bed on which two people can comfortably sleep together. If you have appointed a concubine, she will take one place in this bed and another one will become a "love nest" for a master. There also a two cold floor tiles here.'),
            'house_type': "Premise",
            'upkeep': 27,
            'reconstruction_cost': 90,
            'schedule_options': [('private_bedroom', 'basic_accommodations', 1), ('comfortable_bed', 'basic_accommodations', 1), ('cold_floor', 'basic_accommodations', 2)],
            'resources': {},
            'type': 'room',
        },
        'study': {
            'name': __("Study"),
            "description": __(
                "Reconstruction cost: 80. Upkeep 26. This decent study room provides three office places for work, and two cold floor tiles for sleep."),
            'house_type': "Premise",
            'upkeep': 26,
            'reconstruction_cost': 80,
            'schedule_options': [('cold_floor', 'basic_accommodations', 2)],
            'resources': {'study': 3},
            'type': 'room',
        },

        ##HALLS
        'empty_hall': {
            'name': __("Empty hall"),
            "description": __(
                "Reconstruction cost: Free. Upkeep 32. Empty room gives four free spaces for activities and 16 cold floor tiles."),
            'house_type': "Premise",
            'upkeep': 32,
            'reconstruction_cost': 0,
            'schedule_options': [('cold_floor', 'basic_accommodations', 16)],
            'resources': {'freespace': 4},
            'type': 'hall',
        },
    }


