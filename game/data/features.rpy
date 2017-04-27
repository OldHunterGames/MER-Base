#######################################
#
#	Basic features data
#

 init python:
    person_features = {
    ## GENDER
    'male': {'name': __('male'), 'slot': 'gender', 'modifiers': {'hardiness': +1, 'menace': +1, 'subtlety': -1, 'refinement': -1, 'succulence': -1}, 'image': 'miscards'},
    'female': {'name': __('female'), 'slot': 'gender', 'modifiers': {'hardiness': -1, 'menace': -1, 'subtlety': +1, 'refinement': +1,'succulence': +1}, 'image': 'miscards'},
    'shemale': {'name': __('shemale'), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1, 'hardiness': +1, 'refinement': -1,}, 'image': 'miscards'},
    'transmale': {'name': __('trans'), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1,'succulence': -1}, 'image': 'miscards'},
    'transfemale': {'name': __('androgyn'), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1, 'menace': +1, 'subtlety': -1,'succulence': +1}, 'image': 'miscards'},   

    ## AGE
	'junior': {'name': __('junior'), 'slot': 'age', 'modifiers': {'hardiness': -1, 'menace': -1, 'subtlety': -1, 'refinement': -1, 'competence': -1, 'charisma': +1, 'purity': +1,'succulence': +1}, 'image': 'miscards'},
	'adolescent': {'name': __('adolescent'), 'slot': 'age', 'modifiers': {'menace': -1, 'subtlety': +1, 'competence': -1, 'purity': +1,}, 'image': 'miscards'},
	'mature': {'name': __('mature'), 'slot': 'age', 'modifiers': {'hardiness': +1, 'menace': +1, 'subtlety': -1, 'charisma': +1,}, 'image': 'miscards'},
	'elder': {'name': __('elder'), 'slot': 'age', 'modifiers': {'menace': -1, 'hardiness': -1, 'subtlety': -1,'competence': +1,'extravagance': +1, 'purity': -1, 'refinement': +1, 'succulence': -1}, 'image': 'miscards'},

    ## CONSTITUTION
    'normal': {'name': __('has average build'), 'slot': 'constitution', 'modifiers': {}, 'image': 'miscards'},
    'small': {'name': __('is short'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'menace': -1}, 'image': 'miscards'},
    'large': {'name': __('is tall'), 'slot': 'constitution', 'modifiers': {'menace': +1, 'subtlety': -1}, 'image': 'miscards'},
    'athletic': {'name': __('has athletic build'), 'slot': 'constitution', 'modifiers': {'menace': +1, 'hardiness': +1}, 'image': 'miscards'},
    'brawny': {'name': __('has a broad bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': +1, 'extravagance': +1, 'purity': -1, 'refinement': -1,}, 'image': 'miscards'},
    'lean': {'name': __('has a gracile build'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'hardiness': -1, 'succulence': -1, 'extravagance': -1, 'purity': +1,'refinement': +1,}, 'image': 'miscards'},
    'clumsy': {'name': __('has a disproportional body'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'extravagance': +1, 'purity': -1,'refinement': -1,}, 'image': 'miscards'},
    'crooked': {'name': __('has a crooked bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': -1,'menace': -1, 'extravagance': +1, 'purity': -1,'refinement': -1,}, 'image': 'miscards'},

	## QUIRK
    'stubborn': {'name': __('stubborn'), 'slot': 'quirk', 'modifiers': {'hardiness': +1, 'refinement': -1, 'competence': +1, 'charisma': -1, }, 'image': 'miscards'},
    'sly': {'name': __('sly'), 'slot': 'quirk', 'modifiers': {'hardiness': -1, 'refinement': +1, 'competence': -1, 'charisma': +1, }, 'image': 'miscards'},
    'careless': {'name': __('careless'), 'slot': 'quirk', 'modifiers': {'charisma': +1, 'competence': -1}, 'image': 'miscards'},  
    'scrupulous': {'name': __('scrupulous'), 'slot': 'quirk', 'modifiers': {'charisma': -1,'competence': +1, }, 'image': 'miscards'},        
    'optimistic': {'name': __('optimistic'), 'slot': 'quirk', 'modifiers': {'charisma': +1, }, 'image': 'miscards'},
    'nagging': {'name': __('pessimistic'), 'slot': 'quirk', 'modifiers': {'charisma': -1, }, 'image': 'miscards'},
    'smart': {'name': __('smart'), 'slot': 'quirk', 'modifiers': {'competence': +1}, 'image': 'miscards'},
    'dumb': {'name': __('dumb'), 'slot': 'quirk', 'modifiers': {'competence': -1}, 'image': 'miscards'},

    ## ALIGNMENT
    'timid': {'name': __('timid'), 'slot': 'activity', 'modifiers': {'subtlety': +1, 'menace': -1,}, 'image': 'miscards'},    
    'ardent': {'name': __('ardent'), 'slot': 'activity', 'modifiers': {'menace': +1, 'subtlety': -1,}, 'image': 'miscards'},    
    'lawful': {'name': __('lawful'), 'slot': 'orderliness', 'modifiers': {'competence': +1, 'charisma': -1,}, 'image': 'miscards'},    
    'chaotic': {'name': __('chaotic'), 'slot': 'orderliness', 'modifiers': {'charisma': +1, 'competence': -1,}, 'image': 'miscards'},    
    'good': {'name': __('good'), 'slot': 'morality', 'modifiers': {'purity': +1, 'extravagance': -1,}, 'image': 'miscards'},    
    'evil': {'name': __('evil'), 'slot': 'morality', 'modifiers': {'extravagance': +1, 'purity': -1,}, 'image': 'miscards'}, 
    'unaligned': {'name': __('unaligned'), 'slot': None, 'modifiers': {}, 'image': 'miscards'},    

    ## APPEARENCE
    'unremarkable': {'name': __('appearence is unremarkable'), 'description': __(""), 'slot': 'appearance', 'modifiers': {}, 'image': 'miscards'},    
    'flawless': {'name': __('has a flawless appearence'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'refinement': +1, 'hardiness': -1,}, 'image': 'miscards'},    
    'coarse': {'name': __('looks coarse'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'hardiness': +1, 'refinement': -1,}, 'image': 'miscards'},        
    'unusual': {'name': __('appearence is somehow unusual'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'extravagance': +1, 'purity': -1,}, 'image': 'miscards'},    
    'naive': {'name': __('looks naive'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'purity': +1, 'extravagance': -1,}, 'image': 'miscards'},    
    'gentle': {'name': __('have a gentle appearence'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'charisma': +1, 'menace': -1,}, 'image': 'miscards'},    
    'honest': {'name': __('has a most honest appearence'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'subtlety': -1, 'charisma': +1,}, 'image': 'miscards'},    
    'bold': {'name': __('looks bold'), 'slot': 'appearance', 'description': __(""), 'modifiers': {'subtlety': -1, 'menace': +1,'refinement': +1, 'hardiness': -1,}, 'image': 'miscards'},    
    'wild': {'name': __('looks wild'), 'slot': 'appearance', 'description': __(""), 'modifiers': {'subtlety': -1, 'menace': +1,}, 'image': 'miscards'},    
    'foxy': {'name': __('has a foxy look'), 'slot': 'appearance', 'description': __(""), 'modifiers': {'subtlety': +1, 'charisma': +1,}, 'image': 'miscards'},    
    'sleazy': {'name': __('looks somehow sleazy'), 'description': __(""), 'slot': 'appearance', 'modifiers': {'extravagance': +1, 'purity': -1,'charisma': +1, 'competence': -1,}, 'image': 'miscards'},    
            
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
    
    ## SHAPE
    'emaciated': {'name': __('Emaciated'), 'slot': 'shape', 'modifiers': {'hardiness': -99, 'menace': -2, 'succulence': -2}, 'description': __(""), 'image': 'miscards'},
    'frail': {'name': __('Frail'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'menace': -2 'subtlety': +1, 'refinement': +1}, 'description': __(""), 'image': 'miscards'},
    'slim': {'name': __('Slim'), 'slot': 'shape', 'modifiers': {'menace': -1, 'subtlety': +1, 'succulence': -1}, 'description': __(""), 'image': 'miscards'},
    'wiry': {'name': __('Wiry'), 'slot': 'shape', 'modifiers': {'hardiness': +1,  'subtlety': +1, 'refinement': -1,'succulence': -2}, 'description': __(""), 'image': 'miscards'},
    'skinnyfat': {'name': __('Skinny fat'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'menace': -1, 'refinement': +1,'succulence': +1}, 'description': __(""), 'image': 'miscards'},
    'muscular': {'name': __('Muscular'), 'slot': 'shape', 'modifiers': {'hardiness': +1, 'menace': +1, 'refinement': -1,'succulence': -1}, 'description': __(""), 'image': 'miscards'},
    'flabby': {'name': __('Soft'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'subtlety': -1, 'refinement': +1,'succulence': +2}, 'description': __(""), 'image': 'miscards'},
    'chubby': {'name': __('Chubby'), 'slot': 'shape', 'modifiers': {'menace': +1, 'subtlety': -1, 'succulence': +1}, 'description': __(""), 'image': 'miscards'},
    'beefy': {'name': __('Beefy'), 'slot': 'shape', 'modifiers': {'hardiness': +1, 'menace': +2, 'subtlety': -1, 'refinement': -1}, 'description': __(""), 'image': 'miscards'},
    'obese': {'name': __('Obese'), 'slot': 'shape', 'modifiers': {'hardiness': -1, 'subtlety': -99, 'refinement': -1, 'purity': -1,  'succulence': +1}, 'description': __(""), 'image': 'miscards'},


    #'id': {'name': __('name'), 'slot': 'slot', 'modifiers': {'prosperity': +1}, 'description': __(""), 'image': 'miscards'},
    }


    ## GENDER CORRESPONDENCE

    gender_corrspondence = {
    	'male':'masculine',
    	'female':'feminine',
     	'shemale':'feminine',   
     	'transmale':'feminine',        		    	    	
    	'transfemale':'masculine',
    }

    ## GENUS
    genuses_data = {
        'human':{
            'name': __(''),
            'head_type': 'human',
            'culture': None,
            'modifiers': {},             
            'genders': [('male', 5), ('female', 6), ('transmale', 1), ('transfemale', 1)],
            'ages': [('junior', 1), ('adolescent', 2), ('mature', 3), ('elder', 1)],
            'features': [],
        },
