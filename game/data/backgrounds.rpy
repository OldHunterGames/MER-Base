#######################################
#
#	Basic backgrounds data
#

init python:
    ## HOMEWORLDS 
    
    homeworlds_dict = {
        'default':{
            'name': __('Unknown'),
            'tags': [], 
            'descriptions': [__('{person.name} came out of the Mysts'),]
            
        },    
        'eden':{
            'name': __('Eden'),
            'tags': ['eden'], 
            'descriptions': [__(''), __('wild world 2'), __('wild world 3'), ]
        },
        'sawage':{
            'name': __('Sawage'),
            'tags': ['sawage'],
            'descriptions': [__('prehistoric world 1'), __('prehistoric world 2'), __('prehistoric world 3'), ]
        },
        'lowtec':{
            'name': __('Feudal'),
            'tags': ['notech'],   
            'descriptions': [__('feudal world 1'), __('feudal world 2'), __('feudal world 3'), ]
        },
        'fantasy':{
            'name': __('Fantasy'),
            'tags': ['notech', 'magic'],   
            'descriptions': [__('fantasy world 1'), __('fantasy world 2'), __('fantasy world 3'), ]
        },
        'imperial':{
            'name': __('Imperial'),
            'tags': ['lowtech'],     
            'descriptions': [__('imperial world 1'), __('imperial world 2'), __('imperial world 3'), ]
        },
        'steampunk':{
            'name': __('Steampunk'),
            'tags': ['lowtech', 'weirdscience'], 
            'descriptions': [__('steampunk world 1'), __('steampunk world 2'), __('steampunk world 3'), ]
        },
        'modern':{
            'name': __('Modern'),
            'tags': ['modern'],                    
            'descriptions': [__('modern world 1'), __('modern world 2'), __('modern world 3'), ]
        },
        'cyberpunk':{
            'name': __('Cyberpunk'),
            'tags': ['hightech', 'dystopia'],              
            'descriptions': [__('cyberpunk world 1'), __('cyberpunk world 2'), __('cyberpunk world 3'), ]
        },        
        'postapoc':{
            'name': __('Postapoc'),
            'tags': ['postapoc'],                
            'descriptions': [__('postapoc world 1'), __('postapoc world 2'), __('postapoc world 3'), ]
        },
        'spaceopera':{
            'name': __('Spaceopera'),
            'tags': ['spacetech'],                     
            'descriptions': [__('spaceopera world 1'), __('spaceopera world 2'), __('spaceopera world 3'), ]
        },
    }
    
    ## OCCUOPATIONS 
    
    occupation_features = {

    	## TEMPLATE
        'id': {'name': __('Name'), 
        'description': __("Description"),
        'slot': 'occupation', 
        'tags': ['rome', 'masculine', 'mature', 'menace'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'eastern',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +5, 'hardiness': +1, 'refinement': -1, 'menace': +1, 'subtlety': -1, 'competence': +1, 'charisma': -1, 'extravagance': +1, 'purity': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'loincloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        ## BASIC
        'unknown': {'name': __('Errant'), 
        'description': __(" and has no memory of the past life"),
        'slot': 'occupation', 
        'tags': ['any',],
        'cultures': [], 
        'modifiers': {}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': None, 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'infant': {'name': __('Infantile'), 
        'description': __("and had a life of a careless child"),
        'slot': 'occupation', 
        'tags': ['any', 'junior'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'eastern',],             
        'modifiers': {'sex_buster': -5, 'combat_buster': -5, 'hardiness': -1, 'menace': -1, 'competence': -1, 'purity': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'teenager': {'name': __('Teenager'), 
        'description': __(" and had a common teenager life"),
        'slot': 'occupation', 
        'tags': ['any', 'adolescent'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'eastern',],             
        'modifiers': {}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'retired': {'name': __('Elder'), 
        'description': __(" and retired to the well-deserved rest"),
        'slot': 'occupation', 
        'tags': ['any', 'elder'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'eastern',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': -5, 'hardiness': -1, 'menace': -1, 'competence': +1, 'purity': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },
 

        ## COMMON
        'innocent': {'name': __('Innocent sawage'), 
        'description': __("and had a careless live of innocent sawage"),
        'slot': 'occupation', 
        'tags': ['eden'],
        'cultures': ['native', ],             
        'modifiers': {'sex_buster': -10, 'combat_buster': -10, 'hardiness': +1, 'refinement': -1, 'competence': -1, 'charisma': +1, 'purity': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': None, 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'carnal': {'name': __('Carnal sawage'), 
        'description': __("and had a carnal and wild life"),
        'slot': 'occupation', 
        'tags': ['eden'], 
        'cultures': ['native', ],             
        'modifiers': {'sex_buster': +10, 'combat_buster': +2, 'hardiness': +1, 'refinement': -1, 'menace': +1, 'subtlety': -1, 'competence': -1, 'charisma': +1, 'extravagance': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': None, 'secondary_accessory': None, 'load': None},
        'image': 'miscards',  
        },

        'tribal_hunter': {'name': __('Tribal hunter'), 
        'description': __("and was a common tribal hunter"),
        'slot': 'occupation', 
        'tags': ['sawage'],
        'cultures': ['native',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +5, 'hardiness': +1, 'refinement': -2, 'menace': +1, 'subtlety': -1, 'competence': -1, 'extravagance': +1, 'purity': -1,}, 
        'equipment': {'main_implement': 'stone_spear', 'secondary_implement': None, 'main_accessory': None, 'garment': 'loincloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'tribal_gatherer': {'name': __('Tribal gatherer'), 
        'description': __("and was a common tribal gatherer"),
        'slot': 'occupation', 
        'tags': ['sawage'],
        'cultures': ['native',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +1, 'hardiness': +1, 'refinement': -2, 'competence': -1, 'extravagance': +1, 'purity': -1,}, 
        'equipment': {'main_implement': 'stone_knife', 'secondary_implement': None, 'main_accessory': None, 'garment': 'loincloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        ## ADVANCED


        ## ELITE

    }

