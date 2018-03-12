init python:

    occupations = {
    'vatican': {
    'guard': {'rank': __('hellebardier', 'korporal', 'wachtmeister', 'feldwebel', 'hauptmann', 'oberstleutnant'), 'attribute': 'hardiness',},
    'scholar': {'name': __('apprentice', 'scribe', 'registrar', 'lector', 'librarian', 'archivist',), 'attribute': 'competence',},
    'cleric': {'name': __('novitiate', 'enoch', 'monk', 'cleric', 'vicar', 'abbot',), 'attribute': 'willpower',},
    'missionary': {'name': __('novice', 'pastor', 'preacher', 'hospeller', 'prophet', 'hierophant',), 'attribute': 'grace'},
    'chorus': {'name': __('reserve-singer', 'singer', 'chaplain', 'vizekapellmeister', 'kapellmeister', 'choirmaster',), 'attribute': 'creativity',},
    'inquisitor': {'name': __('apprentice', 'detective', 'custodian', 'inquisitor', 'magister', 'lord-inqusitor',), 'attribute': 'subtlety',},
    },

    }


### УСТАРЕВШАЯ СИСТЕМА
    faction_occupations = {
    'scout': {'name': __('mist scout'), 'attribute': 'hardiness',},
    'artist': {'name': __('artist'), 'attribute': 'creativity',},
    'wisperer': {'name': __('wisperer'), 'attribute': 'subtlety',},
    'engineer': {'name': __('engineer'), 'attribute': 'competence',},
    'trainer': {'name': __('slave trainer'), 'attribute': 'willpower',},
    'courtesan': {'name': __('courtesan'), 'attribute': 'grace', 'gender_exclusive': 'feminine'},
    'jester': {'name': __('jester'), 'attribute': 'grace', 'gender_exclusive': 'masculine'},
    }

    faction_occupation_lvl = [__('an incompetent'),
    __('a novice'),
    __('a competent'),
    __('an established'),
    __('an elite'),
    __('a famous'),
    ]
