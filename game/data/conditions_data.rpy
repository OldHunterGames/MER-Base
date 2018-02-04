init python:
    conditions_data = {
        'misstep': {
            'name': __("Misstep"),
            'description': __("Misstep condition"),
            'type': 'angst',
            'cls_name': "MisstepCondition",
            'slot': 'misstep',
            'modifiers': {'skillcheck': -999}
        },
        'slackness': {
            'name': __("Slackness"),
            'description': __("Slackness condition"),
            'type': 'angst',
            'slot': 'workout',
            'modifiers': {'skillcheck': -999}
        },
        'fatigue': {
            'name': __("Fatigue"),
            'description': __("Fatigue condition"),
            'type': 'angst',
            'slot': 'workout',
            'modifiers': {'skillcheck': -999}
        },
        'hunger': {
            'name': __("Hunger"),
            'description': __("Hunger condition"),
            'type': 'angst',
            'slot': 'satiety',
            'modifiers': {'skillcheck': -999}
        },
        'overeating': {
            'name': __("Overeating"),
            'description': __("Overeating condition"),
            'type': 'angst',
            'slot': 'satiety',
            'modifiers': {'skillcheck': -999}
        },
        'starvation': {
            'name': __("Starvation"),
            'description': __("Starvation condition"),
            'type': 'angst',
            'slot': 'starvation',
            'modifiers': {'skillcheck': -999}
        }
    }