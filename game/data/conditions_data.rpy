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
            'modifiers': {'hardiness': -1}
        },
        'fatigue': {
            'name': __("Fatigue"),
            'description': __("Fatigue condition"),
            'type': 'angst',
            'slot': 'workout',
            'modifiers': {'hardiness': -1}
        },
        'hunger': {
            'name': __("Hunger"),
            'description': __("Hunger condition"),
            'type': 'angst',
            'slot': 'satiety',
            'modifiers': {'hardiness': -1}
        },
        'overeating': {
            'name': __("Overeating"),
            'description': __("Overeating condition"),
            'type': 'angst',
            'slot': 'satiety',
            'modifiers': {'hardiness': -1}
        },
        'starvation': {
            'name': __("Starvation"),
            'description': __("Starvation condition"),
            'type': 'angst',
            'slot': 'starvation',
            'modifiers': {'hardiness': -1}
        }
    }