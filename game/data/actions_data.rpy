init python:
    actions_data = {
        'gamble':{
            'name': __("Gamble"),
            'description': __("Gamble"),
            'lbl': 'lbl_actions_gamble'
        },
        'mist_travel': {
            'name': __("Mist travel"),
            'description': __("Mist travel"),
            'lbl': 'lbl_actions_mist_travel'
        }
    }


label _gamble_fair(person):
    python:
        result = Skillcheck(person, 'subtlety', 3).run()
        if result:
            person.money += 20
        else:
            person.money -= 20
    if result:
        '[person.name] wins 20 sparks'
    else:
        '[person.name] lost 20 sparks'
    return
label lbl_actions_gamble(action):
    python:
        person = action.person
        motivation = UseMotivation(person)
        result = motivation.run()
        if result:
            motivation_type = motivation.used_motivation_type
            if motivation_type == 'enthusiams':
                mode = 'cheat'
            else:
                mode = 'fair'
        else:
            mode = None
    if mode == 'fair':
        call _gamble_fair(person)
    elif mode == 'cheat':
        menu:
            'fair':
                call _gamble_fair(person)
            'cheat':
                $ person.money += 100
                '[person.name] gets 100 sparks'
    else:
        '[person.name] has no motivation'
    return


label lbl_actions_mist_travel(action):
    python:
        worlds = World.get_worlds()
        choice = renpy.display_menu([(i.type, i) for i in worlds])
        MistTravel(core, choice, player).travel()
    return
