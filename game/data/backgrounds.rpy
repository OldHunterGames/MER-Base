#######################################
#
#   Basic backgrounds data
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
            'descriptions': [__('{person.name} originates from a idilstic eden world'), __('{person.name} originates from a lush wild with no hint of civilisation'),]
        },
        'sawage':{
            'name': __('Sawage'),
            'tags': ['sawage'],
            'descriptions': [__('{person.name} originates from prehistoric world 1'), __('{person.name} originates from prehistoric world 2'), __('{person.name} originates from prehistoric world 3'), ]
        },
        'lowtec':{
            'name': __('Feudal'),
            'tags': ['notech'],   
            'descriptions': [__('{person.name} originates from feudal world 1'), __('{person.name} originates from feudal world 2'), __('{person.name} originates from feudal world 3'), ]
        },
        'fantasy':{
            'name': __('Fantasy'),
            'tags': ['notech', 'magic'],   
            'descriptions': [__('{person.name} originates from fantasy world 1'), __('{person.name} originates from fantasy world 2'), __('{person.name} originates from fantasy world 3'), ]
        },
        'imperial':{
            'name': __('Imperial'),
            'tags': ['lowtech'],     
            'descriptions': [__('{person.name} originates from imperial world 1'), __('{person.name} originates from imperial world 2'), __('{person.name} originates from imperial world 3'), ]
        },
        'steampunk':{
            'name': __('Steampunk'),
            'tags': ['lowtech', 'weirdscience'], 
            'descriptions': [__('{person.name} originates from steampunk world 1'), __('{person.name} originates from steampunk world 2'), __('{person.name} originates from steampunk world 3'), ]
        },
        'modern':{
            'name': __('Modern'),
            'tags': ['modern'],                    
            'descriptions': [__('{person.name} originates from modern world 1'), __('{person.name} originates from modern world 2'), __('{person.name} originates from modern world 3'), ]
        },
        'cyberpunk':{
            'name': __('Cyberpunk'),
            'tags': ['hightech', 'dystopia'],              
            'descriptions': [__('{person.name} originates from cyberpunk world 1'), __('{person.name} originates from cyberpunk world 2'), __('{person.name} originates from cyberpunk world 3'), ]
        },        
        'postapoc':{
            'name': __('Postapoc'),
            'tags': ['postapoc'],                
            'descriptions': [__('{person.name} originates from postapoc world 1'), __('{person.name} originates from postapoc world 2'), __('{person.name} originates from postapoc world 3'), ]
        },
        'spaceopera':{
            'name': __('Spaceopera'),
            'tags': ['spacetech'],                     
            'descriptions': [__('{person.name} originates from spaceopera world 1'), __('{person.name} originates from spaceopera world 2'), __('{person.name} originates from spaceopera world 3'), ]
        },
    }
    
    ## OCCUOPATIONS 
    
    occupation_features = {

        ## TEMPLATE
        'id': {'name': __('Name'), 
        'description': __("Description"),
        'nicknames': [ __('nick'), ],
        'slot': 'occupation', 
        'ages': ['junior', 'adolescent', 'mature', 'elder', ],
        'tags': ['rome', 'masculine', 'menace'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +5, 'hardiness': +1, 'competence': +1, 'grace': +1, 'subtlety': +1, 'creativity': +1, 'willpower': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'loincloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        ## BASIC
        'unknown': {'name': __('Errant'), 
        'description': __(" and has no memory of the past life"),
        'slot': 'occupation',
        'ages': ['junior', 'adolescent', 'mature', 'elder', ],         
        'tags': ['any',],
        'cultures': [], 
        'modifiers': {}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': None, 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'infant': {'name': __('Infantile'), 
        'description': __("and had a life of a careless child"),
        'nicknames': [ __('Junior'), ],        
        'slot': 'occupation', 
        'ages': ['junior', ],        
        'tags': ['any'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'sex_buster': -5, 'combat_buster': -5, 'hardiness': -1, 'competence': -1, 'willpower': -1, 'creativity': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'teenager': {'name': __('Teenager'), 
        'description': __(" and had a common teenager life"),
        'nicknames': [ __('Youngster'), ],        
        'slot': 'occupation', 
        'ages': ['adolescent', ],        
        'tags': ['any'],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'retired': {'name': __('Elder'), 
        'description': __(" and retired to the well-deserved rest"),
        'nicknames': [ __('Oldtimer'), ],        
        'slot': 'occupation', 
        'ages': ['elder', ],        
        'tags': ['any', ],
        'cultures': ['western', 'oriental', 'african', 'native', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': -5, 'hardiness': -1, 'grace': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },
 

        ## COMMON
        'innocent': {'name': __('Innocent sawage'), 
        'description': __(" and had a careless live of innocent sawage"),
        'nicknames': [ __('Wildy'), ],        
        'slot': 'occupation', 
        'ages': [],        
        'tags': ['eden'],
        'cultures': ['native', ],             
        'modifiers': {'sex_buster': -10, 'combat_buster': -10, 'hardiness': +1, 'competence': -1, 'subtlety': -1, 'grace': +1, 'willpower': -1, 'creativity': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': None, 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'carnal': {'name': __('Carnal sawage'), 
        'description': __(" and had a carnal and wild life"),
        'nicknames': [ __('Brute'), ],        
        'slot': 'occupation', 
        'ages': [],        
        'tags': ['eden'], 
        'cultures': ['native', ],             
        'modifiers': {'sex_buster': +10, 'combat_buster': +2, 'hardiness': +1, 'subtlety': +1, 'competence': -1, 'grace': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': None, 'secondary_accessory': None, 'load': None},
        'image': 'miscards',  
        },

        'tribal_hunter': {'name': __('Tribal hunter'), 
        'description': __(" and was a common tribal hunter"),
        'nicknames': [ __('Sharp spear'), ],        
        'slot': 'occupation', 
        'ages': [],        
        'tags': ['sawage', 'postapoc'],
        'cultures': ['native',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +5, 'hardiness': +1, 'grace': -1, 'competence': -1,}, 
        'equipment': {'main_implement': 'stone_spear', 'secondary_implement': None, 'main_accessory': None, 'garment': 'loincloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'tribal_gatherer': {'name': __('Tribal gatherer'), 
        'description': __(" and was a common tribal gatherer"),
        'nicknames': [ __('Fingernail'), ],        
        'slot': 'occupation', 
        'ages': [],            
        'tags': ['sawage', 'postapoc'],
        'cultures': ['native',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +1, 'hardiness': +1, 'grace': -1, 'competence': -1,}, 
        'equipment': {'main_implement': 'stone_knife', 'secondary_implement': None, 'main_accessory': None, 'garment': 'loincloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'farmer': {'name': __('Farmer'), 
        'description': __(" and has a life of a simple farmer there"),
        'nicknames': [ __('Dirtfeet'), ],        
        'slot': 'occupation', 
        'ages': [],        
        'tags': ['notech', 'lowtech', 'modern', 'hightech', 'spacetech', ],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'hardiness': +1, 'grace': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': 'knife', 'main_accessory': None, 'garment': 'sturdy_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'factory_worker': {'name': __('Factory worker'), 
        'description': __(" and had a hard working life on a big factory"),
        'nicknames': [ __('Plodder'), ],        
        'slot': 'occupation', 
        'ages': [],         
        'tags': ['lowtech', 'modern', 'hightech', 'spacetech', ],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'hardiness': +1, 'grace': -1, }, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'sturdy_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },
        
        'office_worker': {'name': __('Office worker'), 
        'description': __(" and was a common office worker"),
        'nicknames': [ __('Humster'), ],        
        'slot': 'occupation', 
        'ages': [],                
        'tags': ['modern', 'hightech', 'spacetech', ],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'sex_buster': +5, 'combat_buster': +5, 'hardiness': -1, 'competence': +1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'streetwalker': {'name': __('Streetwalker'), 
        'description': __(" and used to be a streetwalker"),
        'nicknames': [ __('Slut'), ],        
        'slot': 'occupation', 
        'ages': [],               
        'tags': ['notech', 'lowtech', 'modern', 'hightech', 'spacetech', 'feminine', ],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'sex_buster': +10, 'subtlety': +1, 'grace': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'revealing_dress', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'armyman': {'name': __('Armyman'), 
        'description': __(" and used to serve in army"),
        'nicknames': [ __('Warmonger'), ],        
        'slot': 'occupation', 
        'ages': [],           
        'tags': ['notech', 'lowtech', 'modern', 'hightech', 'spacetech', 'masculine'],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'combat_buster': +5, 'hardiness': +1, 'grace': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': 'knife', 'garment': 'military_uniform', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'knave': {'name': __('Knave'), 
        'description': __(" and was a miserable knave there"),
        'slot': 'occupation', 
        'ages': [],               
        'nicknames': [ __('Miser'), ],        
        'tags': ['notech', 'lowtech', 'modern', 'hightech', 'spacetech', ],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'subtlety': +1, 'grace': -1,}, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': 'knife', 'garment': 'casual_cloth', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },

        'performer': {'name': __('Street performer'), 
        'description': __(" earning a living by a street performances"),
        'nicknames': [ __('Flash'), ],        
        'slot': 'occupation', 
        'ages': ['adolescent', 'mature'],        
        'tags': ['notech', 'lowtech', 'modern', 'hightech', 'spacetech', ],
        'cultures': ['western', 'oriental', 'african', 'nordic', 'slavic', 'arabic',],             
        'modifiers': {'sex_buster': +2, 'competence': -1, 'grace': +1, }, 
        'equipment': {'main_implement': None, 'secondary_implement': None, 'main_accessory': None, 'garment': 'revealing_dress', 'secondary_accessory': None, 'load': None},
        'image': 'miscards',
        },


        ## ADVANCED


        ## ELITE

    }

