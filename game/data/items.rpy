﻿####################################
#
#   Basic items data
#

init python:

    ## TAGS DESCRIPTION

    # lethal - can be used as a weapon, leaves wound, opponent can be killed
    # nonlethal - can be used as a weapon, leaves bruises, opponent will live
    # heavy - can be equpped to a main_implement slot and blocks secondary_implement slots
    # versatile - can be equpped to a main_implement and secondary_implement slots
    # shield - can be equpped to a secondary_implement slot 
    # offhand - can be equpped to a main_implement, secondary_implement and accessory slots, cannot be equipped in a load slot
    # hard_armor - counts as a hard armor, can be equipped in garment slot and blocks secondary_implement slot
    # soft_armor - counts as a soft armor, can be equipped in garment slot
    # garment - counts as unarmored, can be equipped in garment slot
    # accessory - can be equipped in accessory slots, cannot be equipped in a load slot
    # load - can be equipped into a load slot only, but fully functional when equiped there 
    # mutable - item name and descriprtion can be edited by player

    ## TEMPLATE ITEM

    template_data = {
        'id':{
            'name': __("Name"),
            'description': __('Description.'),
            'quality': 1,  
            'size': 1,  
            'condition': 5, 
            'modifiers': {'hardiness': +1, 'refinement': -1, 'menace': +1, 'subtlety': -1, 'competence': +1, 'charisma': -1, 'extravagance': +1, 'purity': -1},
            'tags': ['accessory', ],                             
        },
    }

    ## Implement type items

    heavy_wapon_data = {
        'halberd':{
            'name': __("Halberd"),
            'description': __('Heavy and fearsome longreach battlefield class weapon.'),
            'quality': 2,  
            'size': 10,  
            'condition': 5, 
            'modifiers': {'refinement': -1, 'menace': +2, 'subtlety': -99, 'purity': -1},
            'tags': ['lethal', 'heavy', ],                             
        },

        'stone_spear':{
            'name': __("Stone spear"),
            'description': __('Spear with a stone tip. Crude but effective heavy melee weapon.'),
            'quality': 1,  
            'size': 5,  
            'condition': 5, 
            'modifiers': {'refinement': -99, 'menace': +1, 'subtlety': -99, 'extravagance': +1, 'purity': -1},
            'tags': ['lethal', 'heavy', ],                             
        },

    }

    versatile_weapon_data = {

    }

    offhand_weapon_data = {

        'stone_knife':{
            'name': __("Stone knife"),
            'description': __('Spear with a stone tip. Crude but effective heavy melee weapon.'),
            'quality': 1,  
            'size': 1,  
            'condition': 5, 
            'modifiers': {'hardiness': +1},
            'tags': ['lethal', 'offhand', ],                             
        },

        'knife': {
            'name': __("Stone knife"),
            'description': __('Spear with a stone tip. Crude but effective heavy melee weapon.'),
            'quality': 1,  
            'size': 1,  
            'condition': 5, 
            'modifiers': {'hardiness': +1},
            'tags': ['lethal', 'offhand', ],          
        }
        


    }

    heavy_implement_data = {

    }

    versatile_implement_data = {

    }

    offhand_implement_data = {

    }

    ## Garment type items

    garment_data = {
        'rags':{
            'name': __("Tattered clothes"),
            'description': __('This clothes are ruined beyond any good use. Not good for your image.'),
            'quality': 1,  
            'size': 1,  
            'condition': 0, 
            'modifiers': {'refinement': -99, 'charisma': -99, 'menace': -2, 'purity': -1},
            'tags': ['garment', ],                             
        },

        'casual_cloth':{
            'name': __("Casual cloth"),
            'description': __('Just a simple cloth, noting special.'),
            'quality': 2,  
            'size': 3,  
            'condition': 5, 
            'modifiers': {'menace': -1, },
            'tags': ['garment', ],                             
        },
        
        'loincloth':{
            'name': __("Loincloth"),
            'description': __('Just a humble loincloth, do not covers much.'),
            'quality': 1,  
            'size': 1,  
            'condition': 5, 
            'modifiers': {'refinement': -99, 'menace': -2, 'subtlety': +1, 'extravagance': +1, 'purity': -1},
            'tags': ['accessory', ],                             
        },

        'revealing_dress' : {},
        'sturdy_cloth': {}

    }

    armor_data = {

    }

    ## Loadout type items

    loadout_data = {

    }


    ## Accessory type items

    accessory_data = {
        'jewel':{
            'name': __("jewel"),
            'description': __('This piece of jewelry contains a clear gem, suited to store the Sparks.'),
            'price': 10,
            'mutable_name': True,
            'mutable_description': False
        },
    }


    ## Unequipible items

    item_data = {

    }