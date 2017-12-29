init python:
    actions_data = {
        'gamble':{
            'name': __("Gamble"),
            'description': __("Gamble"),
            'lbl': 'lbl_actions_gamble'
        }
    }



label lbl_actions_gamble(action):
    python:
        user = action.user