init python:

    occupations = {
    'vatican': {
    'guard': {'rank': {'0': __('hellebardier'), '1': __('korporal'), '2': __('wachtmeister'), '3': __('feldwebel'), '4': __('hauptmann'), '5': __('oberstleutnant')}, 'attribute': 'hardiness',},
    'scholar': {'name': {'0': __('apprentice'), '1': __('scribe'), '2': __('registrar'), '3': __('lector'), '4': __('librarian'), '5': __('archivist'),}, 'attribute': 'competence',},
    'cleric': {'name': {'0': __('novitiate'), '1': __('enoch'), '2': __('monk'), '3': __('cleric'), '4': __('vicar'), '5': __('abbot'),}, 'attribute': 'willpower', },
    'missionary': {'name': {'0': __('novice'), '1': __('pastor'), '2': __('preacher'), '3': __('hospeller'), '4': __('prophet'), '5': __('hierophant'),}, 'attribute': 'grace'},
    'chorus': {'name': {'0': __('reserve-singer'), '1': __('singer'), '2': __('chaplain'), '3': __('vizekapellmeister'), '4': __('kapellmeister'), '5': __('choirmaster'),}, 'attribute': 'creativity',},
    'inquisitor': {'name': {'0': __('apprentice'), '1': __('detective'), '2': __('custodian'), '3': __('inquisitor'), '4': __('magister'), '5': __('lord-inqusitor'),}, 'attribute': 'subtlety',},
    },

    }

    core_factions = {
        'vatican': {
            'name': __("Vatican"),
            'description': __("Vatican faction"),
            'check_person': lambda person: person.age != 'child' and person.genus.id == 'human'
        }
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
