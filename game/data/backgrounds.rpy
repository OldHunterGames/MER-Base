#######################################
#
#	Basic backgrounds data
#

init python:
        
    ## HOMEWORLDS 
    
    homeworlds_dict = {
    'wild': {
            'name': __('wild'),
            'properties': ['wild'],
            'cultures': ['primitive',],
            'genuses': ['human',],
            'features': ['ignorant'], 
            'modifiers': {'purity': +1,}
            'descriptions': [__('wild world 1'), __('wild world 2'), __('wild world 3'), ]
        },

    'fantasy': {
            'name': __('fantasy'),
            'properties': ['wild'],
            
            'cultures': ['fantasy',],
            'genuses': ['human',],
            'features': ['ignorant', ], 
            'modifiers': {'purity': +1,}
            'descriptions': [__('fantasy world 1'), __('fantasy world 2'), __('fantasy world 3'), ]
        },

    }