####################################
#
#   Basic features data
#

 init python:
    person_features = {
    ## GENDER
    'male': {'name': __('male'), 'description': __(" male"), 'slot': 'gender', 'modifiers': {'hardiness': +1, 'menace': +1, 'subtlety': -1, 'refinement': -1, 'succulence': -1}, 'image': 'miscards'},
    'female': {'name': __('female'), 'description': __(" female"), 'slot': 'gender', 'modifiers': {'hardiness': -1, 'menace': -1, 'subtlety': +1, 'refinement': +1,'succulence': +1}, 'image': 'miscards'},
    'shemale': {'name': __('shemale'), 'description': __(" shemale"), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1, 'hardiness': +1, 'refinement': -1,}, 'image': 'miscards'},
    'transmale': {'name': __('trans'), 'description': __(" transmale"), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1,'succulence': -1}, 'image': 'miscards'},
    'transfemale': {'name': __('androgyn'), 'description': __(" transfemale"), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1, 'menace': +1, 'subtlety': -1,'succulence': +1}, 'image': 'miscards'},   

    ## AGE
    'junior': {'name': __('junior'), 'description': __(" junior"), 'slot': 'age', 'modifiers': {'hardiness': -1, 'menace': -1, 'subtlety': -1, 'refinement': -1, 'competence': -1, 'charisma': +1, 'purity': +1,'succulence': +1}, 'image': 'miscards'},
    'adolescent': {'name': __('adolescent'), 'description': __(" adolescent"), 'slot': 'age', 'modifiers': {'menace': -1, 'subtlety': +1, 'competence': -1, 'purity': +1,}, 'image': 'miscards'},
    'mature': {'name': __('mature'), 'description': __(" mature"), 'slot': 'age', 'modifiers': {'hardiness': +1, 'menace': +1, 'subtlety': -1, 'charisma': +1,}, 'image': 'miscards'},
    'elder': {'name': __('elder'), 'description': __(" elder"), 'slot': 'age', 'modifiers': {'menace': -1, 'hardiness': -1, 'subtlety': -1,'competence': +1,'extravagance': +1, 'purity': -1, 'refinement': +1, 'succulence': -1}, 'image': 'miscards'},

    ## CONSTITUTION
    'normal': {'name': __('has average build'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},
    'small': {'name': __('is short'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'menace': -1}, 'image': 'miscards'},
    'large': {'name': __('is tall'), 'slot': 'constitution', 'modifiers': {'menace': +1, 'subtlety': -1}, 'image': 'miscards'},
    'athletic': {'name': __('has athletic build'), 'slot': 'constitution', 'modifiers': {'menace': +1, 'hardiness': +1}, 'image': 'miscards'},
    'brawny': {'name': __('has a broad bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': +1, 'extravagance': +1, 'purity': -1, 'refinement': -1,}, 'image': 'miscards'},
    'lean': {'name': __('has a gracile build'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'hardiness': -1, 'succulence': -1, 'extravagance': -1, 'purity': +1,'refinement': +1,}, 'image': 'miscards'},
    'clumsy': {'name': __('has a disproportional body'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'extravagance': +1, 'purity': -1,'refinement': -1,}, 'image': 'miscards'},
    'crooked': {'name': __('has a crooked bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': -1,'menace': -1, 'extravagance': +1, 'purity': -1,'refinement': -1,}, 'image': 'miscards'},
    'amorphous': {'name': __('has amorphous body'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},
    'shapeshifter': {'name': __('is a shapeshifter'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},

    ## QUIRK
    'stubborn': {'name': __('stubborn'), 'description': __(" {person.name} is appearently stubborn."), 'slot': 'quirk', 'modifiers': {'hardiness': +1, 'refinement': -1, 'competence': +1, 'charisma': -1, }, 'image': 'miscards'},
    'sly': {'name': __('sly'), 'description': __(" {person.name} is quite sly."), 'slot': 'quirk', 'modifiers': {'hardiness': -1, 'refinement': +1, 'competence': -1, 'charisma': +1, }, 'image': 'miscards'},
    'careless': {'name': __('careless'), 'description': __(" {person.name} is appearently careless."), 'slot': 'quirk', 'modifiers': {'charisma': +1, 'competence': -1}, 'image': 'miscards'},  
    'scrupulous': {'name': __('scrupulous'), 'description': __(" {person.name} is quite scrupulous."), 'slot': 'quirk', 'modifiers': {'charisma': -1,'competence': +1, }, 'image': 'miscards'},        
    'optimistic': {'name': __('optimistic'), 'description': __(" {person.name} looks optimistic most of the time."), 'slot': 'quirk', 'modifiers': {'charisma': +1, }, 'image': 'miscards'},
    'nagging': {'name': __('pessimistic'), 'description': __(" {person.name} is irritatingly nagging and grumpy person."), 'slot': 'quirk', 'modifiers': {'charisma': -1, }, 'image': 'miscards'},
    'smart': {'name': __('smart'), 'description': __(" {person.name} is quite smart."), 'slot': 'quirk', 'modifiers': {'competence': +1}, 'image': 'miscards'},
    'dumb': {'name': __('dumb'), 'description': __(" {person.name} is dumb as a stump."), 'slot': 'quirk', 'modifiers': {'competence': -1}, 'image': 'miscards'},

    ## ALIGNMENT
    'timid': {'name': __('timid'), 'slot': 'activity', 'modifiers': {'subtlety': +1, 'menace': -1,}, 'image': 'miscards'},    
    'ardent': {'name': __('ardent'), 'slot': 'activity', 'modifiers': {'menace': +1, 'subtlety': -1,}, 'image': 'miscards'},    
    'lawful': {'name': __('lawful'), 'slot': 'orderliness', 'modifiers': {'competence': +1, 'charisma': -1,}, 'image': 'miscards'},    
    'chaotic': {'name': __('chaotic'), 'slot': 'orderliness', 'modifiers': {'charisma': +1, 'competence': -1,}, 'image': 'miscards'},    
    'good': {'name': __('good'), 'slot': 'morality', 'modifiers': {'purity': +1, 'extravagance': -1,}, 'image': 'miscards'},    
    'evil': {'name': __('evil'), 'slot': 'morality', 'modifiers': {'extravagance': +1, 'purity': -1,}, 'image': 'miscards'}, 
    'unaligned': {'name': __('conformal'), 'slot': None, 'modifiers': {}, 'image': 'miscards'},    

    ## APPEARENCE
    'unremarkable': {'name': __('Unremarkable'), 'description': __("appearence is unremarkable"), 'slot': 'appearance', 'modifiers': {}, 'image': 'miscards'},    
    'flawless': {'name': __('Flawless'), 'description': __("has a flawless appearence"), 'slot': 'appearance', 'modifiers': {'refinement': +1, 'hardiness': -1,}, 'image': 'miscards'},    
    'coarse': {'name': __('Coarse'), 'description': __("looks coarse"), 'slot': 'appearance', 'modifiers': {'hardiness': +1, 'refinement': -1,}, 'image': 'miscards'},        
    'unusual': {'name': __('Unusual'), 'description': __("appearence is somehow unusual"), 'slot': 'appearance', 'modifiers': {'extravagance': +1, 'purity': -1,}, 'image': 'miscards'},    
    'naive': {'name': __('Naive'), 'description': __("looks naive"), 'slot': 'appearance', 'modifiers': {'purity': +1, 'extravagance': -1,}, 'image': 'miscards'},    
    'gentle': {'name': __('Gentle'), 'description': __("have a gentle appearence"), 'slot': 'appearance', 'modifiers': {'charisma': +1, 'menace': -1,}, 'image': 'miscards'},    
    'honest': {'name': __('Honest'), 'description': __("has a most honest appearence"), 'slot': 'appearance', 'modifiers': {'subtlety': -1, 'charisma': +1,}, 'image': 'miscards'},    
    'bold': {'name': __('Bold'), 'slot': 'appearance', 'description': __("looks bold"), 'modifiers': {'subtlety': -1, 'menace': +1,'refinement': +1, 'hardiness': -1,}, 'image': 'miscards'},    
    'wild': {'name': __('Wild'), 'slot': 'appearance', 'description': __("looks wild"), 'modifiers': {'subtlety': -1, 'menace': +1,}, 'image': 'miscards'},    
    'foxy': {'name': __('Foxy'), 'slot': 'appearance', 'description': __("has a foxy look"), 'modifiers': {'subtlety': +1, 'charisma': +1,}, 'image': 'miscards'},    
    'sleazy': {'name': __('Sleazy'), 'description': __("looks somehow sleazy"), 'slot': 'appearance', 'modifiers': {'extravagance': +1, 'purity': -1,'charisma': +1, 'competence': -1,}, 'image': 'miscards'},    
            
    ## NEEDS
    'greedy': {'name': __('greedy'), 'slot': 'prosperity_feat', 'modifiers': {'prosperity': +1}, 'description': __("{person.name}is {{color=#00ffcc}}greedy{{/color}}, wich makes {pronoun2} sensitive to prosperity matters."), 'image': 'miscards'},
    'generous': {'name': __('generous'), 'slot': 'prosperity_feat', 'modifiers': {'prosperity': -1}, 'description': __("{person.name}is {{color=#ff9999}}generous{{/color}}, so {pronoun} is not concerned by {possesive} own prosperity."), 'image': 'miscards'},
    'gourmet': {'name': __('gourmet'), 'slot': 'nutrition_feat', 'modifiers': {'nutrition': +1}, 'description': __("{person.name}is a true {{color=#00ffcc}}gourmet{{/color}}, and food is a priority for {pronoun2}."), 'image': 'miscards'},
    'moderate_eater': {'name': __('moderate eater'), 'slot': 'nutrition_feat', 'modifiers': {'nutrition': -1}, 'description': __("Being a {{color=#ff9999}}moderate eater{{/color}}, {pronoun} have no interest in delicacies but can easily endure crappy nutrition."), 'image': 'miscards'},
    'sensitive': {'name': __('sensitive'), 'slot': 'wellness_feat', 'modifiers': {'wellness': +1}, 'description': __("{cap_pronoun} is {{color=#00ffcc}}sensitive{{/color}} and concerned by {possesive} body wellness."), 'image': 'miscards'},
    'enduring': {'name': __('enduring'), 'slot': 'wellness_feat', 'modifiers': {'wellness': -1}, 'description': __("{cap_pronoun} can easily {{color=#ff9999}}endure{{/color}} flesh suffering and have a little concernes about wellness of the body."), 'image': 'miscards'},
    'sybarite': {'name': __('sybarite'), 'slot': 'comfort_feat', 'modifiers': {'comfort': +1}, 'description': __("{person.name}is a {{color=#00ffcc}}sybarite{{/color}}, and values comfort a lot."), 'image': 'miscards'},
    'ascetic': {'name': __('ascetic'), 'slot': 'comfort_feat', 'modifiers': {'comfort': -1}, 'description': __("{person.name}is {{color=#ff9999}}ascetic{{/color}}, and finds comfort useless."), 'image': 'miscards'},
    'energetic': {'name': __('energetic'), 'slot': 'activity_feat', 'modifiers': {'activity': +1}, 'description': __("{person.name}burting with {{color=#00ffcc}}energy{{/color}}, and needs adrenaline."), 'image': 'miscards'},
    'lazy': {'name': __('lazy'), 'slot': 'activity_feat', 'modifiers': {'activity': -1}, 'description': __("{person.name}is {{color=#ff9999}}lazy{{/color}}, and needs no trill or adremaline."), 'image': 'miscards'},
    'extrovert': {'name': __('extrovert'), 'slot': 'communication_feat', 'modifiers': {'communication': +1}, 'description': __("{person.name}is an {{color=#00ffcc}}extravert{{/color}}, in constant need for communication."), 'image': 'miscards'},
    'introvert': {'name': __('introvert'), 'slot': 'communication_feat', 'modifiers': {'communication': -1}, 'description': __("{person.name}is an {{color=#ff9999}}introvert{{/color}}, needs less communication than the average person."), 'image': 'miscards'},
    'curious': {'name': __('curious'), 'slot': 'amusement_feat', 'modifiers': {'amusement': +1}, 'description': __("{cap_pronoun} is a {{color=#00ffcc}}curious{{/color}} person, and loves amusement."), 'image': 'miscards'},
    'dull': {'name': __('dull'), 'slot': 'amusement_feat', 'modifiers': {'amusement': -1}, 'description': __("{cap_pronoun} is a {{color=#ff9999}}dull{{/color}} person, and can do without entertainment."), 'image': 'miscards'},
    'leader': {'name': __('leader'), 'slot': 'authority_feat', 'modifiers': {'authority': +1}, 'description': __("In everyday life {pronoun} tends to be a {{color=#00ffcc}}leader{{/color}}, and walues autority ower other people."), 'image': 'miscards'},
    'liberal': {'name': __('liberal'), 'slot': 'authority_feat', 'modifiers': {'authority': -1}, 'description': __("{pronoun} have a {{color=#ff9999}}liberal{{/color}} vision, and have no taste for autority ower other people. "), 'image': 'miscards'},
    'ambitious': {'name': __('ambitious'), 'slot': 'ambition_feat', 'modifiers': {'ambition': +1}, 'description': __("{cap_pronoun} is a very {{color=#00ffcc}}ambitious{{/color}} and wants to be the best in everything."),'image': 'miscards' },
    'modest': {'name': __('modest'), 'slot': 'ambition_feat', 'modifiers': {'ambition': -1}, 'description': __("{cap_pronoun} is a {{color=#ff9999}}modest{{/color}} person and have no need to approve own ambitions constantly."), 'image': 'miscards'},
    'lewd': {'name': __('sensual'), 'slot': 'eros_feat', 'modifiers': {'eros': +1}, 'description': __("{person.name}is quite {{color=#00ffcc}}sensual{{/color}} and has a wild erotic fantasies."), 'image': 'miscards'},
    'frigid': {'name': __('frigid'), 'slot': 'eros_feat', 'modifiers': {'eros': -1}, 'description': __("{person.name}is quite {{color=#ff9999}}frigid{{/color}} and have almost no sex drive."), 'image': 'miscards'},

    ## METABOLISM
    #'metabolism_food': {'name': __('name'), 'slot': 'metabolism', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    #'id': {'name': __('name'), 'slot': 'metabolism', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    #'id': {'name': __('name'), 'slot': 'metabolism', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    
    ## SHAPE
    'emaciated': {'name': __('Emaciated'), 'slot': 'shape', 'modifiers': {'hardiness': -99, 'menace': -2, 'succulence': -2}, 'description': __("and emaciated to the limit"), 'image': 'miscards'},
    'frail': {'name': __('Frail'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'menace': -2, 'subtlety': +1, 'refinement': +1}, 'description': __("and in frail shape"), 'image': 'miscards'},
    'slim': {'name': __('Slim'), 'slot': 'shape', 'modifiers': {'menace': -1, 'subtlety': +1, 'succulence': -1}, 'description': __("and in slim shape"), 'image': 'miscards'},
    'wiry': {'name': __('Wiry'), 'slot': 'shape', 'modifiers': {'hardiness': +1,  'subtlety': +1, 'refinement': -1,'succulence': -2}, 'description': __("with a dry and wiry muscles"), 'image': 'miscards'},
    'skinnyfat': {'name': __('Skinny fat'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'menace': -1, 'refinement': +1,'succulence': +1}, 'description': __("amd looks like a skinny-fat"), 'image': 'miscards'},
    'undistinguished': {'name': __(''), 'slot': 'shape', 'modifiers': {}, 'description': __(""), 'image': 'miscards'},
    'muscular': {'name': __('Muscular'), 'slot': 'shape', 'modifiers': {'hardiness': +1, 'menace': +1, 'refinement': -1,'succulence': -1}, 'description': __("and wery fit"), 'image': 'miscards'},
    'flabby': {'name': __('Soft'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'subtlety': -1, 'refinement': +1,'succulence': +2}, 'description': __("with a smooth body"), 'image': 'miscards'},
    'chubby': {'name': __('Chubby'), 'slot': 'shape', 'modifiers': {'menace': +1, 'subtlety': -1, 'succulence': +1}, 'description': __("with a chubby curves"), 'image': 'miscards'},
    'beefy': {'name': __('Beefy'), 'slot': 'shape', 'modifiers': {'hardiness': +1, 'menace': +2, 'subtlety': -1, 'refinement': -1}, 'description': __("with a beefy torso"), 'image': 'miscards'},
    'obese': {'name': __('Obese'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'subtlety': -99, 'refinement': -1, 'purity': -1,  'succulence': +1}, 'description': __("and visibily obeese"), 'image': 'miscards'},

    #'id': {'name': __('name'), 'slot': 'slot', 'modifiers': {'hardiness': +1, 'refinement': -1, 'menace': +1, 'subtlety': -1, 'competence': +1, 'charisma': -1, 'extravagance': +1, 'purity': -1}, 'description': __(""), 'image': 'miscards'},
    }


    ## GENDER CORRESPONDENCE

    gender_correspondence = {
        'male':'masculine',
        'female':'feminine',
        'shemale':'feminine',   
        'transmale':'feminine',                             
        'transfemale':'masculine',
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
            'head_type': 'human',
            'culture': None,
        },

        'ghoul':{
            'name': __('ghoul'),
            'description': __('undead ghoul'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {},             
            'tags': ['ageless'], 
            'features': [],
            'head_type': 'undead',
            'culture': None,
        },

        'doghead':{
            'name': __('doghead'),
            'description': __('furry'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {},             
            'tags': [], 
            'features': [],
            'head_type': 'canine',
            'culture': None,
        },

        'slimegirl':{
            'name': __('slimegirl'),
            'description': __('slimegirl'),
            'slot': 'genus', 
            'image': 'miscards',  
            'modifiers': {},             
            'tags': [], 
            'features': ['ageless', 'sexless'],
            'head_type': 'canine',
            'culture': None,
        },

    }
