#######################################
#
#	Basic features data
#

 init python:
    person_features = {
    ## GENDER
    'male': {'name': __('male'), 'slot': 'gender', 'modifiers': {'hardiness': +1, 'menace': +1, 'subtlety': -1, 'refinement': -1, 'succulence': -1}},
    'female': {'name': __('female'), 'slot': 'gender', 'modifiers': {'hardiness': -1, 'menace': -1, 'subtlety': +1, 'refinement': +1,'succulence': +1}},
    'shemale': {'name': __('shemale'), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1, 'hardiness': +1, 'refinement': -1,}},
    'transmale': {'name': __('trans'), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1,'succulence': -1}},
    'transfemale': {'name': __('androgyn'), 'slot': 'gender', 'modifiers': {'extravagance': +1, 'purity': -1, 'menace': +1, 'subtlety': -1,'succulence': +1}},   


    ## AGE
	'junior': {'name': __('junior'), 'slot': 'age', 'modifiers': {'hardiness': -1, 'menace': -1, 'subtlety': -1, 'refinement': -1, 'competence': -1, 'charisma': +1, 'purity': +1,'succulence': +1}},
	'adolescent': {'name': __('adolescent'), 'slot': 'age', 'modifiers': {'menace': -1, 'subtlety': +1, 'competence': -1, 'purity': +1,}},
	'mature': {'name': __('mature'), 'slot': 'age', 'modifiers': {'hardiness': +1, 'menace': +1, 'subtlety': -1, 'charisma': +1,}},
	'elder': {'name': __('elder'), 'slot': 'age', 'modifiers': {'menace': -1, 'hardiness': -1, 'subtlety': -1,'competence': +1,'extravagance': +1, 'purity': -1, 'refinement': +1, 'succulence': -1}},

    ## CONSTITUTION
    'normal': {'name': __('has average build'), 'slot': 'constitution', 'modifiers': {}},
    'small': {'name': __('is short'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'menace': -1}},
    'large': {'name': __('is tall'), 'slot': 'constitution', 'modifiers': {'menace': +1, 'subtlety': -1}},
    'athletic': {'name': __('has athletic build'), 'slot': 'constitution', 'modifiers': {'menace': +1, 'hardiness': +1}},
    'brawny': {'name': __('has a broad bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': +1, 'extravagance': +1, 'purity': -1, 'refinement': -1,}},
    'lean': {'name': __('has a gracile build'), 'slot': 'constitution', 'modifiers': {'subtlety': +1, 'hardiness': -1, 'succulence': -1, 'extravagance': -1, 'purity': +1,'refinement': +1,}},
    'clumsy': {'name': __('has a disproportional body'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'extravagance': +1, 'purity': -1,'refinement': -1,}},
    'crooked': {'name': __('has a crooked bones'), 'slot': 'constitution', 'modifiers': {'subtlety': -1, 'hardiness': -1,'menace': -1, 'extravagance': +1, 'purity': -1,'refinement': -1,}},

	## QUIRK
    'stubborn': {'name': __('stubborn'), 'slot': 'quirk', 'modifiers': {'hardiness': +1, 'refinement': -1, 'competence': +1, 'charisma': -1, }},
    'sly': {'name': __('sly'), 'slot': 'quirk', 'modifiers': {'hardiness': -1, 'refinement': +1, 'competence': -1, 'charisma': +1, }},
    'careless': {'name': __('careless'), 'slot': 'quirk', 'modifiers': {'charisma': +1, 'competence': -1}},  
    'scrupulous': {'name': __('scrupulous'), 'slot': 'quirk', 'modifiers': {'charisma': -1,'competence': +1, }},        
    'optimistic': {'name': __('optimistic'), 'slot': 'quirk', 'modifiers': {'charisma': +1, }},
    'nagging': {'name': __('pessimistic'), 'slot': 'quirk', 'modifiers': {'charisma': -1, }},
    'smart': {'name': __('smart'), 'slot': 'quirk', 'modifiers': {'competence': +1}},
    'dumb': {'name': __('dumb'), 'slot': 'quirk', 'modifiers': {'competence': -1}},

    ## ALIGNMENT
    'timid': {'name': __('timid'), 'slot': 'activity', 'modifiers': {'subtlety': +1, 'menace': -1,}},    
    'ardent': {'name': __('ardent'), 'slot': 'activity', 'modifiers': {'menace': +1, 'subtlety': -1,}},    
    'lawful': {'name': __('lawful'), 'slot': 'orderliness', 'modifiers': {'competence': +1, 'charisma': -1,}},    
    'chaotic': {'name': __('chaotic'), 'slot': 'orderliness', 'modifiers': {'charisma': +1, 'competence': -1,}},    
    'good': {'name': __('good'), 'slot': 'morality', 'modifiers': {'purity': +1, 'extravagance': -1,}},    
    'evil': {'name': __('evil'), 'slot': 'morality', 'modifiers': {'extravagance': +1, 'purity': -1,}}, 
    'conformal': {'name': __('conformal'), 'slot': None, 'modifiers': {'': +1, '': -1,}},    

    'id': {'name': __('name'), 'slot': 'appearance', 'modifiers': {'subtlety': +1, 'menace': -1,}},    


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
            'genders': [('male', 5), ('female', 6), ('transmale', 1), ('transfemale', 1)],
            'ages': [('junior', 1), ('adolescent', 2), ('mature', 3), ('elder', 1)],
            'features': [],
        },
