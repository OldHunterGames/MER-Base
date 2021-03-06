﻿####################################
#
#   Basic features data
#

 init python:
    person_features = {
    ## GENDER
    'male': {'name': __('male'), 'description': __(" male"), 'slot': 'gender', 'modifiers': {'hardiness': +1, 'willpower': +1, 'subtlety': -1, 'grace': -1, 'succulence': -1}, 'image': 'miscards'},
    'female': {'name': __('female'), 'description': __(" female"), 'slot': 'gender', 'modifiers': {'hardiness': -1, 'willpower': -1, 'subtlety': +1, 'grace': +1,'succulence': +1}, 'image': 'miscards'},
    'shemale': {'name': __('shemale'), 'description': __(" shemale"), 'slot': 'gender', 'modifiers': {}, 'image': 'miscards'},
    'transmale': {'name': __('trans'), 'description': __(" transmale"), 'slot': 'gender', 'modifiers': {'hardiness': +1, 'grace': -1, 'succulence': -1}},
    'transfemale': {'name': __('androgyn'), 'description': __(" transfemale"), 'slot': 'gender', 'modifiers': {'hardiness': -1, 'grace': +1, 'succulence': +1}, 'image': 'miscards'},   

    ## AGE
    'junior': {'name': __('junior'), 'description': __(" junior"), 'slot': 'age', 'modifiers': {'hardiness': -1, 'willpower': -1,  'subtlety': -1, 'creativity': +1,'grace': +1, 'competence': -1, 'succulence': +1}, 'image': 'miscards'},
    'adolescent': {'name': __('adolescent'), 'description': __(" adolescent"), 'slot': 'age', 'modifiers': {'hardiness': -1, 'subtlety': +1, 'competence': -1, 'grace': +1,}, 'image': 'miscards'},
    'mature': {'name': __('mature'), 'description': __(" mature"), 'slot': 'age', 'modifiers': {'hardiness': +1, 'competence': +1, 'willpower': +1, 'grace': -1,}, 'image': 'miscards'},
    'elder': {'name': __('elder'), 'description': __(" elder"), 'slot': 'age', 'modifiers': {'hardiness': -1,'competence': +1, 'willpower': +1, 'creativity': -1, 'grace': -1, 'succulence': -1}, 'image': 'miscards'},

    ## CONSTITUTION
    'normal': {'name': __('average constitution'), 'description': __('has average build'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},
    'small': {'name': __('short'), 'nicknames': [ __('Little one'), ],  'description': __('is short'),  'slot': 'constitution', 'modifiers': {'subtlety': +1, 'hardiness': -1}, 'image': 'miscards'},
    'large': {'name': __('tall'), 'nicknames': [ __('Big one'), ],  'description': __('is tall'), 'slot': 'constitution', 'modifiers': {'hardiness': +1, 'subtlety': -1}, 'image': 'miscards'},
    'athletic': {'name': __('athletic'), 'nicknames': [ __('Statutory'), ],  'description': __('has athletic build'), 'slot': 'constitution', 'modifiers': {'hardiness': +1}, 'image': 'miscards'},
    'brawny': {'name': __('broad bones'), 'nicknames': [ __('Stocky'), ],  'description': __('has a broad bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': +1, 'grace': -1}, 'image': 'miscards'},
    'lean': {'name': __('gracile'), 'nicknames': [ __('Grace'), ],  'description': __('has a gracile build'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'hardiness': -1, 'succulence': -1, 'grace': +1,}, 'image': 'miscards'},
    'clumsy': {'name': __('disproportional body'), 'nicknames': [ __('Awkward'), ],  'description': __('has a disproportional body'), 'slot': 'constitution', 'modifiers': {'grace': -1,}, 'image': 'miscards'},
    'crooked': {'name': __('crooked'), 'nicknames': [ __('Shriveled'), ],  'description': __('has a crooked bones'), 'slot': 'constitution', 'modifiers': {'grace': -2, 'hardiness': -1,}, 'image': 'miscards'},
    'amorphous': {'name': __('amorphous body'), 'description': __('has amorphous body'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},
    'shapeshifter': {'name': __('shapeshifter'), 'description': __('is a shapeshifter'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},

    ## QUIRK
    'stubborn': {'name': __('stubborn'), 'nicknames': [ __('Dogged'), ], 'description': __(" {person.name} is appearently stubborn."), 'slot': 'quirk', 'modifiers': {'willpower': +1, 'grace': -1, }, 'image': 'miscards'},
    'sly': {'name': __('sly'), 'nicknames': [ __('Slimy'), ], 'description': __(" {person.name} is quite sly."), 'slot': 'quirk', 'modifiers': {'hardiness': -1, 'subtlety': +1, }, 'image': 'miscards'},
    'careless': {'name': __('careless'), 'nicknames': [ __('Loony'), ], 'description': __(" {person.name} is appearently careless."), 'slot': 'quirk', 'modifiers': {'grace': +1, 'competence': -1}, 'image': 'miscards'},  
    'scrupulous': {'name': __('scrupulous'), 'nicknames': [ __('Meticulous'), ], 'description': __(" {person.name} is quite scrupulous."), 'slot': 'quirk', 'modifiers': {'creativity': -1,'competence': +1, }, 'image': 'miscards'},        
    'optimistic': {'name': __('optimistic'), 'nicknames': [ __('Happy-go-lucky'), ], 'description': __(" {person.name} looks optimistic most of the time."), 'slot': 'quirk', 'modifiers': {'willpower': +1, }, 'image': 'miscards'},
    'nagging': {'name': __('pessimistic'), 'nicknames': [ __('Grouchy'), ], 'description': __(" {person.name} is irritatingly nagging and grumpy person."), 'slot': 'quirk', 'modifiers': {'willpower': -1, }, 'image': 'miscards'},
    'smart': {'name': __('smart'), 'nicknames': [ __('Brainy'), ], 'description': __(" {person.name} is quite smart."), 'slot': 'quirk', 'modifiers': {'competence': +1}, 'image': 'miscards'},
    'dumb': {'name': __('dumb'), 'nicknames': [ __('Dumbass'), ], 'description': __(" {person.name} is dumb as a stump."), 'slot': 'quirk', 'modifiers': {'competence': -1}, 'image': 'miscards'},

    ## ALIGNMENT
    'timid': {'name': __('{{color=#00ffcc}}timid{{/color}}'), 'nicknames': [ __('Calm'), ], 'slot': 'activity', 'modifiers': {'competence': +1, 'hardiness': -1,}, 'image': 'miscards'},
    'ardent': {'name': __('{{color=#ff9999}}ardent{{/color}}'), 'nicknames': [ __('Fervent'), ], 'slot': 'activity', 'modifiers': {'hardiness': +1, 'competence': -1,}, 'image': 'miscards'},
    'lawful': {'name': __('{{color=#00ffcc}}lawful{{/color}}'), 'nicknames': [ __('Decent'), ], 'slot': 'orderliness', 'modifiers': {'willpower': +1, 'creativity': -1,}, 'image': 'miscards'},
    'chaotic': {'name': __('{{color=#ff9999}}chaotic{{/color}}'), 'nicknames': [ __('Incalculable'), ], 'slot': 'orderliness', 'modifiers': {'creativity': +1, 'willpower': -1,}, 'image': 'miscards'},
    'good': {'name': __('{{color=#00ffcc}}good{{/color}}'), 'nicknames': [ __('Kind'), __('Goodkind'), __('Nicey'), ], 'slot': 'morality', 'modifiers': {'grace': +1, 'subtlety': -1,}, 'image': 'miscards'},
    'evil': {'name': __('{{color=#ff9999}}evil{{/color}}'), 'nicknames': [ __('Malicious'), __('Fiend'), __('Vicious'), __('Hellkite'), ], 'slot': 'morality', 'modifiers': {'subtlety': +1, 'grace': -1,}, 'image': 'miscards'},
    'unaligned': {'name': __('conformal'), 'slot': None, 'modifiers': {}, 'image': 'miscards'},    

    ## APPEARENCE
    'unremarkable': {'name': __('Unremarkable'), 'description': __("{cap_possesive} appearence is unremarkable"), 'slot': 'appearance', 'modifiers': {}, 'image': 'miscards'},    
    'flawless': {'name': __('Flawless'), 'nicknames': [ __('Irreproachable'), ], 'description': __("{cap_pronoun} has a flawless appearence"), 'slot': 'appearance', 'modifiers': {'grace': +1,}, 'image': 'miscards'},    
    'coarse': {'name': __('Coarse'), 'nicknames': [ __('Rude'), ], 'description': __("{cap_pronoun} looks coarse"), 'slot': 'appearance', 'modifiers': {'hardiness': +1, 'grace': -1,}, 'image': 'miscards'},        
    'unusual': {'name': __('Unusual'), 'nicknames': [ __('Strange One'), ], 'description': __("{cap_possesive} appearence is somehow unusual"), 'slot': 'appearance', 'modifiers': {'creativity': +1, 'grace': -1,}, 'image': 'miscards'},    
    'naive': {'name': __('Naive'), 'nicknames': [ __('Simpleton'), ], 'description': __("{cap_pronoun} looks naive"), 'slot': 'appearance', 'modifiers': {'grace': +1, 'willpower': -1,}, 'image': 'miscards'},    
    'gentle': {'name': __('Gentle'), 'nicknames': [ __('Dendilion'), ], 'description': __("{cap_pronoun} have a gentle appearence"), 'slot': 'appearance', 'modifiers': {'grace': +1, 'hardiness': -1,}, 'image': 'miscards'},    
    'honest': {'name': __('Honest'), 'description': __("{cap_pronoun} has a most honest appearence"), 'slot': 'appearance', 'modifiers': {'subtlety': -1, 'grace': +1,}, 'image': 'miscards'},    
    'bold': {'name': __('Bold'), 'nicknames': [ __('Rock'), ], 'slot': 'appearance', 'description': __("{cap_pronoun} looks bold"), 'modifiers': {'subtlety': -1, 'hardiness': +1,}, 'image': 'miscards'},    
    'wild': {'name': __('Wild'), 'nicknames': [ __('Wildheart'), ], 'slot': 'appearance', 'description': __("{cap_pronoun} looks wild"), 'modifiers': {'grace': -1, 'hardiness': +1,}, 'image': 'miscards'},    
    'foxy': {'name': __('Foxy'), 'nicknames': [ __('Canny'), ], 'slot': 'appearance', 'description': __("{cap_pronoun} has a foxy look"), 'modifiers': {'subtlety': +1,}, 'image': 'miscards'},    
    'sleazy': {'name': __('Sleazy'), 'nicknames': [ __('Saucy'), ], 'description': __("{cap_pronoun} looks somehow sleazy"), 'slot': 'appearance', 'modifiers': {'subtlety': +1, 'hardiness': -1,  'willpower': -1, 'creativity': +1,}, 'image': 'miscards'},    
            
    ## NEEDS
    'greedy': {'name': __('greedy'), 'nicknames': [ __('Grabber'), ], 'slot': 'prosperity_feat', 'modifiers': {'prosperity': +1}, 'description': __("{person.name} is {{color=#00ffcc}}greedy{{/color}}, wich makes {pronoun2} sensitive to prosperity matters. "), 'image': 'miscards'},
    'generous': {'name': __('generous'), 'nicknames': [ __('Lavish'), ], 'slot': 'prosperity_feat', 'modifiers': {'prosperity': -1}, 'description': __("{person.name} is {{color=#ff9999}}generous{{/color}}, so {pronoun} is not concerned by {possesive} own prosperity. "), 'image': 'miscards'},
    'gourmet': {'name': __('gourmet'), 'nicknames': [ __('Glutton'), ], 'slot': 'nutrition_feat', 'modifiers': {'nutrition': +1}, 'description': __("{person.name} is a true {{color=#00ffcc}}gourmet{{/color}}, and food is a priority for {pronoun2}. "), 'image': 'miscards'},
    'moderate_eater': {'name': __('moderate eater'), 'slot': 'nutrition_feat', 'modifiers': {'nutrition': -1}, 'description': __("Being a {{color=#ff9999}}moderate eater{{/color}}, {pronoun} have no interest in delicacies but can easily endure crappy nutrition. "), 'image': 'miscards'},
    'sensitive': {'name': __('sensitive'), 'nicknames': [ __('Flower'), ], 'slot': 'wellness_feat', 'modifiers': {'wellness': +1}, 'description': __("{cap_pronoun} is {{color=#00ffcc}}sensitive{{/color}} and concerned by {possesive} body wellness. "), 'image': 'miscards'},
    'enduring': {'name': __('enduring'), 'nicknames': [ __('Hardy'), ], 'slot': 'wellness_feat', 'modifiers': {'wellness': -1}, 'description': __("{cap_pronoun} can easily {{color=#ff9999}}endure{{/color}} flesh suffering and have a little concernes about wellness of the body. "), 'image': 'miscards'},
    'sybarite': {'name': __('sybarite'), 'nicknames': [ __('Voluptuary'), ], 'slot': 'comfort_feat', 'modifiers': {'comfort': +1}, 'description': __("{person.name} is a {{color=#00ffcc}}sybarite{{/color}}, and values comfort a lot. "), 'image': 'miscards'},
    'ascetic': {'name': __('ascetic'), 'nicknames': [ __('Saint Crow'), ], 'slot': 'comfort_feat', 'modifiers': {'comfort': -1}, 'description': __("{person.name} is {{color=#ff9999}}ascetic{{/color}}, and finds comfort useless. "), 'image': 'miscards'},
    'energetic': {'name': __('energetic'), 'nicknames': [ __('Perky'), ], 'slot': 'activity_feat', 'modifiers': {'activity': +1}, 'description': __("{person.name} burting with {{color=#00ffcc}}energy{{/color}}, and needs adrenaline. "), 'image': 'miscards'},
    'lazy': {'name': __('lazy'), 'nicknames': [ __('Sloth'), ], 'slot': 'activity_feat', 'modifiers': {'activity': -1}, 'description': __("{person.name} is {{color=#ff9999}}lazy{{/color}}, and needs no trill or adremaline. "), 'image': 'miscards'},
    'extrovert': {'name': __('extrovert'), 'nicknames': [ __('Matey'), ], 'slot': 'communication_feat', 'modifiers': {'communication': +1}, 'description': __("{person.name} is an {{color=#00ffcc}}extravert{{/color}}, in constant need for communication. "), 'image': 'miscards'},
    'introvert': {'name': __('introvert'), 'nicknames': [ __('Offish'), ], 'slot': 'communication_feat', 'modifiers': {'communication': -1}, 'description': __("{person.name} is an {{color=#ff9999}}introvert{{/color}}, needs less communication than the average person. "), 'image': 'miscards'},
    'curious': {'name': __('curious'), 'nicknames': [ __('Nosey'), ], 'slot': 'amusement_feat', 'modifiers': {'amusement': +1}, 'description': __("{cap_pronoun} is a {{color=#00ffcc}}curious{{/color}} person, and loves amusement. "), 'image': 'miscards'},
    'dull': {'name': __('dull'), 'nicknames': [ __('Tedious'), ], 'slot': 'amusement_feat', 'modifiers': {'amusement': -1}, 'description': __("{cap_pronoun} is a {{color=#ff9999}}dull{{/color}} person, and can do without entertainment. "), 'image': 'miscards'},
    'leader': {'name': __('leader'), 'nicknames': [ __('Dominus'), ], 'slot': 'authority_feat', 'modifiers': {'authority': +1}, 'description': __("In everyday life {cap_pronoun} tends to be a {{color=#00ffcc}}leader{{/color}}, and walues autority ower other people. "), 'image': 'miscards'},
    'liberal': {'name': __('liberal'), 'nicknames': [ __('Lenient'), ], 'slot': 'authority_feat', 'modifiers': {'authority': -1}, 'description': __("{cap_pronoun} have a {{color=#ff9999}}liberal{{/color}} vision, and have no taste for autority ower other people. "), 'image': 'miscards'},
    'ambitious': {'name': __('ambitious'), 'nicknames': [ __('Winner'), ], 'slot': 'ambition_feat', 'modifiers': {'ambition': +1}, 'description': __("{cap_pronoun} is a very {{color=#00ffcc}}ambitious{{/color}} and wants to be the best in everything. "),'image': 'miscards' },
    'modest': {'name': __('modest'), 'nicknames': [ __('Demure'), ], 'slot': 'ambition_feat', 'modifiers': {'ambition': -1}, 'description': __("{cap_pronoun} is a {{color=#ff9999}}modest{{/color}} person and have no need to approve own ambitions constantly. "), 'image': 'miscards'},
    'lewd': {'name': __('sensual'), 'nicknames': [ __('Horny'), ], 'slot': 'eros_feat', 'modifiers': {'eros': +1}, 'description': __("{person.name} is quite {{color=#00ffcc}}sensual{{/color}} and has a wild erotic fantasies. "), 'image': 'miscards'},
    'frigid': {'name': __('frigid'), 'nicknames': [ __('Coldfish'), ], 'slot': 'eros_feat', 'modifiers': {'eros': -1}, 'description': __("{person.name} is quite {{color=#ff9999}}frigid{{/color}} and have almost no sex drive. "), 'image': 'miscards'},

    ## METABOLISM
    #'metabolism_food': {'name': __('name'), 'slot': 'metabolism', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    #'id': {'name': __('name'), 'slot': 'metabolism', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    #'id': {'name': __('name'), 'slot': 'metabolism', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    
    ## SHAPE
    'emaciated': {'name': __('Emaciated'), 'slot': 'shape', 'modifiers': {'hardiness': -99, 'succulence': -2}, 'description': __("and emaciated to the limit"), 'image': 'miscards'},
    'frail': {'name': __('Frail'), 'slot': 'shape', 'modifiers': {'hardiness': -1, }, 'description': __("and in frail shape"), 'image': 'miscards'},
    'slim': {'name': __('Slim'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'grace': +1, 'succulence': -1}, 'description': __("and in slim shape"), 'image': 'miscards'},
    'wiry': {'name': __('Wiry'), 'slot': 'shape', 'modifiers': {'subtlety': +1, 'succulence': -2}, 'description': __("with a dry and wiry muscles"), 'image': 'miscards'},
    'skinnyfat': {'name': __('Skinny fat'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'succulence': +1}, 'description': __("amd looks like a skinny-fat"), 'image': 'miscards'},
    'undistinguished': {'name': __(''), 'slot': 'shape', 'modifiers': {}, 'description': __(""), 'image': 'miscards'},
    'muscular': {'name': __('Muscular'), 'slot': 'shape', 'modifiers': {'hardiness': +1, 'grace': -1,'succulence': -1}, 'description': __("and wery fit"), 'image': 'miscards'},
    'flabby': {'name': __('Soft'), 'slot': 'shape', 'modifiers': {'grace': -1, 'subtlety': -1,'succulence': +2}, 'description': __("with a smooth body"), 'image': 'miscards'},
    'chubby': {'name': __('Chubby'), 'slot': 'shape', 'modifiers': {'hardiness': +1, 'succulence': +1}, 'description': __("with a chubby curves"), 'image': 'miscards'},
    'beefy': {'name': __('Beefy'), 'slot': 'shape', 'modifiers': {'hardiness': +2, 'subtlety': -1, 'grace': -1,}, 'description': __("with a beefy torso"), 'image': 'miscards'},
    'obese': {'name': __('Obese'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'grace': -99, 'subtlety': -1, 'succulence': +1}, 'description': __("and visibily obeese"), 'image': 'miscards'},

    #'id': {'name': __('name'), 'slot': 'slot', 'modifiers': {'hardiness': +1, 'competence': -1, 'subtlety': -1, 'grace': +1, 'creativity': +1, 'willpower': -1, 'succulence': +1}, 'description': __(""), 'image': 'miscards'},
    }


    ## GENDER CORRESPONDENCE

    gender_correspondence = {
        'male':'masculine',
        'female':'feminine',
        'shemale':'feminine',   
        'transmale':'feminine',                             
        'transfemale':'masculine',
        'sexless': 'feminine',
    }

    ## GENUS
    genuses_data = {
        'human':{
            'name': __('common human'),
            'description': __(''),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {},             
            'tags': [], 
            'features': [],
            'default_items': {'secondary_implement': 'bare_hands', 'garment': 'nude', }, 
            'head_type': 'human',
            'culture': None,
        },
        
        'fey':{
            'name': __('fey'),
            'description': __('fey'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {},             
            'tags': ['ageless'], 
            'features': [],
            'default_items': {'secondary_implement': 'bare_hands', 'garment': 'nude', }, 
            'head_type': 'fairy',
            'culture': None,
        },

        'ghoul':{
            'name': __('ghoul'),
            'description': __('undead ghoul'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {'succulence': -99, },             
            'tags': ['ageless'], 
            'features': [],
            'default_items': {'secondary_implement': 'bare_hands', 'garment': 'nude', }, 
            'head_type': 'undead',
            'culture': None,
        },

        'doghead':{
            'name': __('doghead'),
            'description': __('furry'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {'menace': +1, 'willpower': +1, 'creativity': -1, 'grace': -1, },             
            'tags': ['ageless'], 
            'features': [],
            'default_items': {'secondary_implement': 'bare_hands', 'garment': 'fur', }, 
            'head_type': 'canine',
            'culture': None,
        },

        'slimegirl':{
            'name': __('slimegirl'),
            'description': __('slimegirl'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {},             
            'tags': ['ageless', 'sexless'], 
            'features': [],
            'head_type': 'slime',
            'culture': None,
        },

    }


    sexual_orientation = {'asexual': {'name': __('asexual'), 'male': -1, 'female': -1, 'description': __('finds sexual inrecourse disgusting.')}, 
    'omisexual': {'name': __('omisexual'), 'male': 0, 'female': 0, 'description': __("has no preference for a partner's gender.")}, 
    'straight_female': {'name': __('straight'), 'male': 1, 'female': -1, 'description': __('loves males, and turned off by females.')}, 
    'straight_male': {'name': __('straight'), 'male': -1, 'female': 1, 'description': __('loves females, and turned off by males.')}, 
    'gay': {'name': __('gay'), 'male': 1, 'female': -1, 'description': __('loves males, and turned off by females.')}, 
    'lesbian': {'name': __('lesbian'), 'male': -1, 'female': 1, 'description': __('loves females, and turned off by males.')}, 
    'bicurious_male': {'name': __('bi-curious'), 'male': 0, 'female': 1, 'description': __('prefers females more than a males.')}, 
    'bicurious_female': {'name': __('bi-curious'), 'male': 1, 'female': 0, 'description': __('prefers males more than a females.')}, 
    'bisexual': {'name': __('bisexual'), 'male': 1, 'female': 1, 'description': __('loves both males and females.')}, 
    }
        
    sexual_type = {
        'dissolute': {'name': __("dissolute"), 'description': __("loves anything as long as it is even remotely sexy!"), 
            'active': {'rough': 1, 'tender': 1, 'passionate': 1, 'bizarre': 1}, 
            'receiving': {'rough': 1, 'tender': 1, 'passionate': 1, 'bizarre': 1}, 
            },               
        'worn': {'name': __("worn out"), 'description': __("have seen everything, not interested in anything."), 
            'active': {'rough': 0, 'tender': 0, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': 0, 'tender': 0, 'passionate': 0, 'bizarre': 0}, 
            },
        'frigid': {'name': __("frigid"), 'description': __("accepts incoming tenderness somehow, but turned off by anything else."), 
            'active': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': -1}, 
            'receiving': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': -1}, 
            },            
        'modest': {'name': __("modest"), 'description': __("thinks that tenderness is okay, but bizarre, rough or even overpassionate sex is disgusting."), 
            'active': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': -1}, 
            'receiving': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': -1}, 
            },   
        'vanilla': {'name': __("vanilla"), 'description': __("loves to recive tenderness and passion, but despites all rough and bizarre actions."), 
            'active': {'rough': -1, 'tender': 0, 'passionate': 0, 'bizarre': -1}, 
            'receiving': {'rough': -1, 'tender': 1, 'passionate': 1, 'bizarre': -1}, 
            },       
        'macho': {'name': __("macho"), 'description': __("loves to recive tenderness and passion, despites to rcive rough and bizarre actions, but loves to act rough and passionate."), 
            'active': {'rough': +1, 'tender': 0, 'passionate': +1, 'bizarre': 0}, 
            'receiving': {'rough': -1, 'tender': 1, 'passionate': 1, 'bizarre': -1}, 
            },    
        'caring': {'name': __("caring"), 'description': __("calmly accepts any treatment, but never whants to be rough or bizzare by itself. Carries only a passion and tenderness for a partner."), 
            'active': {'rough': -1, 'tender': 1, 'passionate': 1, 'bizarre': -1}, 
            'receiving': {'rough': 0, 'tender': 0, 'passionate': 0, 'bizarre': 0}, 
            },       
        'gentle': {'name': __("gentle one"), 'description': __("loves all tender interactions, but turned off by rough and bizarre actions."), 
            'active': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': -1}, 
            'receiving': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': -1}, 
            },       
        'suitor': {'name': __("suitor"), 'description': __("loves to be gentle and tender with a partner, and do not want to be rough. Turned off by anything bizarre."), 
            'active': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': -1}, 
            'receiving': {'rough': 0, 'tender': 0, 'passionate': 0, 'bizarre': -1}, 
            },       
        'narcissistic': {'name': __("narcissistic"), 'description': __("truly appreciates tender treatment. Can be gentle itself if needed and accepts passion somehow, but hates any rough and bizarre stuff and have no passion for a patner at all."), 
            'active': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': -1}, 
            'receiving': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': -1}, 
            },                               
        'passionate': {'name': __("passionate"), 'description': __("loves all passionate interactions, but turned off by bizarre and tender actions."), 
            'active': {'rough': 0, 'tender': -1, 'passionate': 1, 'bizarre': -1}, 
            'receiving': {'rough': 0, 'tender': -1, 'passionate': 1, 'bizarre': -1}, 
            },       
        'lewd': {'name': __("lewd"), 'description': __("loves sex, be it tender or passionate, and open minded for some bizzare or rouht action."), 
            'active': {'rough': 0, 'tender': 1, 'passionate': 1, 'bizarre': 0}, 
            'receiving': {'rough': 0, 'tender': 1, 'passionate': 1, 'bizarre': 0}, 
            },       
        'vtop': {'name': __("vanilla top"), 'description': __("caries active passion for a partner but turned of by rough response or any bizarre stuff."), 
            'active': {'rough': 0, 'tender': 0, 'passionate': 1, 'bizarre': -1}, 
            'receiving': {'rough': -1, 'tender': 0, 'passionate': 0, 'bizarre': -1}, 
            },       
        'vbottom': {'name': __("vanilla bottom"), 'description': __("loves to recieve passion, but turned off by a bizzare stuff. Do not like to be rough."), 
            'active': {'rough': -1, 'tender': 0, 'passionate': 0, 'bizarre': -1}, 
            'receiving': {'rough': 0, 'tender': 0, 'passionate': 1, 'bizarre': -1}, 
            },       
        'active': {'name': __("active"), 'description': __("loves to be active and do everything (and anything!) by itself. Accepts not passionete, rough or bizzare actions from a partners side."), 
            'active': {'rough': 1, 'tender': 1, 'passionate': 1, 'bizarre': 1}, 
            'receiving': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': -1}, 
            },       
        'passive': {'name': __("passive"), 'description': __("loves to recieve attention (any attention!), but turned off if something passionate, rough or bizzare need to be done by itself."), 
            'active': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': -1}, 
            'receiving': {'rough': 1, 'tender': 1, 'passionate': 1, 'bizarre': 1}, 
            },       
        'sadist': {'name': __("sadist"), 'description': __("loves to be rough and recive tenderness in response, but turned off by reverse situations."), 
            'active': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': 0}, 
            },     
        'masochist': {'name': __("masochist"), 'description': __("loves to be tender and recive rough treatment in response, but turned off by reverse situations."), 
            'active': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            },     
        'sadomazo': {'name': __("sadomazo"), '': __("loves rough actions bothways, but turned off by any tenderness."), 
            'active': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            },     
        'strict_sadist': {'name': __("black sadist"), 'description': __("just loves to be rough, and, frankly, not interested in anything else."), 
            'active': {'rough': 1, 'tender': 0, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': 0, 'tender': 0, 'passionate': 0, 'bizarre': 0}, 
            },     
        'strict_masochist': {'name': __("black masochist"), 'description': __("just loves to recive rough treatment, and, frankly, not interested in anything else."), 
            'active': {'rough': -1, 'tender': 1, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            },     
        'strict_sadomazo': {'name': __("black sadomazo"), 'description': __("loves rough actions bothways and, frankly, not interested in anything else."), 
            'active': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': -1, 'passionate': 0, 'bizarre': 0}, 
            },     
        'dominant': {'name': __("dominant"), 'description': __("loves to be passionate and rough, but do not tolerates same actions in response and preferes tender partners."), 
            'active': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 0}, 
            'receiving': {'rough': -1, 'tender': 1, 'passionate': -1, 'bizarre': 0}, 
            },       
        'submissive': {'name': __("submissive"), 'description': __("loves to recieve rough and passionate treatment, but prefers to be gentle by itself."), 
            'active': {'rough': -1, 'tender': 1, 'passionate': -1, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 0}, 
            },                                 
        'bizzare_dominant': {'name': __("bizarre dominant"), 'description': __("loves to be passionate, rough and do a bizarre stuff, but do not tolerates roughness and passion in response."), 
            'active': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 1}, 
            'receiving': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': 1}, 
            },       
        'bizzare_submissive': {'name': __("bizarre submissive"), 'description': __("loves to recieve rough and passionate treatment, do a bizarre stuff, but do not like to be rough or passionate itself."), 
            'active': {'rough': -1, 'tender': 0, 'passionate': -1, 'bizarre': 1}, 
            'receiving': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 1}, 
            },                     
        'switch': {'name': __("switch"), 'description': __("loves all rough and passionate interactions, but turned off by tenderness."), 
            'active': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 0}, 
            },     
        'kniky': {'name': __("kinky"), 'description': __("loves all rough, bizarre and passionate interactions."), 
            'active': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 1}, 
            'receiving': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 1}, 
            },    
        'wild_kinky': {'name': __("wild and kinky"), 'description': __("loves all rough, bizarre and passionate interactions, but turned off by a dull common tenderness."), 
            'active': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 1}, 
            'receiving': {'rough': 1, 'tender': 0, 'passionate': 1, 'bizarre': 1}, 
            },    
        'tender_switch': {'name': __("tender switch"), 'description': __("loves all rough and passionate interactions, but loves tenderness too!"), 
            'active': {'rough': 1, 'tender': 1, 'passionate': 1, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': 1, 'passionate': 1, 'bizarre': 0}, 
            },                
        'wild': {'name': __("wild"), 'description': __("loves all rough and passionate interactions, but turned off by tenderness."), 
            'active': {'rough': 1, 'tender': -1, 'passionate': 1, 'bizarre': 0}, 
            'receiving': {'rough': 1, 'tender': -1, 'passionate': 1, 'bizarre': 0}, 
            },                       
        'deviant': {'name': __("deviant"), 'description': __("loves bizarre sex, but turned off by a dull common tenderness."), 
            'active': {'rough': 0, 'tender': -1, 'passionate': 0, 'bizarre': 1}, 
            'receiving': {'rough': 0, 'tender': -1, 'passionate': 0, 'bizarre': 1}, 
            },        
        'freak': {'name': __("freak"), 'description': __("is tuned on by anything bizarre and truned off by anything else."), 
            'active': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': 1}, 
            'receiving': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': 1}, 
            },        
        'loony': {'name': __("loony"), 'description': __("is tuned on by doing bizarre actions and truned off by anything else."), 
            'active': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': 1}, 
            'receiving': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': -1}, 
            },                    
        'weirdo': {'name': __("weirdo"), 'description': __("is a weirdo indeed, tuned on by receiving bizarre actions and truned off by anything else."), 
            'active': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': 1}, 
            'receiving': {'rough': -1, 'tender': -1, 'passionate': -1, 'bizarre': -1}, 
            },                     
    }

    anatomy_features = {
        'penis': 
            {
            'name': __("Penis"), 
            "description": __("{self.penis_size.name} {self.penis_type.name}"), 
            'slot': 'penis', 
            'parts': ['penis_size', 'penis_type'],
            'basis': True,
            'sensitive': True,
            'stimulating': False,
            'penetration': 'penetrative'},
        'horse_penis': {'name': __("horse penis"), 'slot': 'penis_type'},
        'canine_penis': {'name': __("canine penis"), 'slot': 'penis_type'},        
        'human_penis': {'name': __("cock"), 'slot': 'penis_type'},

        'micro_penis': {"name": __("diminutive"), 'slot': 'penis_size', 'modifiers': {'size': 1}},
        'small_penis': {"name": __("small"), 'slot': 'penis_size', 'modifiers': {'size': 2}},        
        'normal_penis': {"name": __("normal"), 'slot': 'penis_size', 'modifiers': {'size': 3}},
        'large_penis': {"name": __("large"), 'slot': 'penis_size', 'modifiers': {'size': 4}},        
        'huge_penis': {"name": __("huge"), 'slot': 'penis_size', 'modifiers': {'size': 5}},          

        'vagina': 
            {
            'name': __("vagina"), 
            "description": __("{self.vagina_wetness.name}{self.vagina_size.name}"), 
            'slot': 'vagina', 
            'parts': ['vagina_size'],
            'basis': True,
            'sensitive': True,
            'stimulating': False,
            'penetration': 'receiving'},
        'micro_vagina': {"name": __("very tight pussy"), 'slot': 'vagina_size', 'modifiers': {'size': 1}},
        'small_vagina': {"name": __("tight pussy"), 'slot': 'vagina_size', 'modifiers': {'size': 2}},        
        'normal_vagina': {"name": __("reasonably tigh pussy"), 'slot': 'vagina_size', 'modifiers': {'size': 3}},
        'large_vagina': {"name": __("loose pussy"), 'slot': 'vagina_size', 'modifiers': {'size': 4}},        
        'huge_vagina': {"name": __("gaping vaginal hole"), 'slot': 'vagina_size', 'modifiers': {'size': 5}},          

        'dry_vagina': {"name": __("dry and "), 'slot': 'vagina_wetness', 'modifiers': {'wetness': -1}},
        'wet_vagina': {"name": __("juicy and"), 'slot': 'vagina_wetness', 'modifiers': {'wetness': 1}},

        'ass': 
            {
            'name': __("asshole"), 
            "description": __("{self.ass_size.name}"), 
            'slot': 'ass', 
            'parts': ['ass_size'],
            'basis': True,
            'sensitive': False,
            'stimulating': True,
            'penetration': 'receiving'},
        'micro_ass': {"name": __("very tight anus"), 'slot': 'ass_size', 'modifiers': {'size': 1}},
        'small_ass': {"name": __("nice and tight anus"), 'slot': 'ass_size', 'modifiers': {'size': 2}},        
        'normal_ass': {"name": __("reasonably tigh anus"), 'slot': 'ass_size', 'modifiers': {'size': 3}},
        'large_ass': {"name": __("loose anus"), 'slot': 'ass_size', 'modifiers': {'size': 4}},        
        'huge_ass': {"name": __("gaping anal spincter"), 'slot': 'ass_size', 'modifiers': {'size': 5}},   

        'boobs': 
            {
            'name': __("boobs"), 
            "description": __("{self.boobs_size.name}"), 
            'slot': 'boobs', 
            'parts': ['boobs_size'],
            'basis': True,
            'sensitive': False,
            'stimulating': False,
            'penetration': False},
        'micro_boobs': {"name": __("flat chest"), 'slot': 'boobs_size', 'modifiers': {'size': 1}},
        'small_boobs': {"name": __("small breasts"), 'slot': 'boobs_size', 'modifiers': {'size': 2}},        
        'normal_boobs': {"name": __("fair tits"), 'slot': 'boobs_size', 'modifiers': {'size': 3}},
        'large_boobs': {"name": __("large boobs"), 'slot': 'boobs_size', 'modifiers': {'size': 4}},        
        'huge_boobs': {"name": __("enormous udders"), 'slot': 'boobs_size', 'modifiers': {'size': 5}},   

        'mouth': 
            {
            'name': __("mouth"), 
            "description": __("normal mouth"), 
            'slot': 'mouth', 
            'parts': [],
            'basis': True,
            'sensitive': False,
            'stimulating': True,
            'penetration': False},

        'body': 
            {
            'name': __("body"), 
            "description": __(""), 
            'slot': 'body', 
            'parts': [],
            'basis': True,
            'sensitive': False,
            'stimulating': False,
            'penetration': False},

        'manipulator': 
            {
            'name': __("mouth"), 
            "description": __("{self.appendage.name}"), 
            'slot': 'mouth', 
            'parts': ['appendage'],
            'basis': True,
            'sensitive': False,
            'stimulating': False,
            'penetration': False},        

        'human_hand': {"name": __("human hands"), 'slot': 'appendage', 'modifiers': {}},                                                

        'foot': 
            {
            'name': __("foot"), 
            "description": __("{self.pedal.name}"), 
            'slot': 'foot', 
            'parts': ['pedal'],
            'basis': True,
            'sensitive': False,
            'stimulating': False,
            'penetration': False},        

        'human_foot': {"name": __("human feets"), 'slot': 'pedal', 'modifiers': {},     

    }
    }

