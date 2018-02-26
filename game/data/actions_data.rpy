init python:
    actions_data = {
        'gamble':{
            'name': __("Gamble"),
            'description': __("Gamble"),
            'lbl': 'lbl_actions_gamble'
        },
        'bazar':{
            'name': __("Bazar"),
            'description': __("Go for some trades"),
            'lbl': 'lbl_actions_bazar'
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
            if motivation_type == 'enthusiasm':
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

init python:
    class BazarBuy(object):
        type = 'buy'
        def __init__(self, item, price):
            self.item = item
            self.price = price

    class BazarSell(BazarBuy):
        type = 'sell'

label lbl_actions_bazar(action):
    python:
        person = action.person
        worlds = World.get_worlds()
        choices = [('Gem(%s) - 10 sparks'%i.type, BazarBuy(i, 10)) for i in worlds if person.has_money(10)]
        if person.has_money(10):
            choices.append((__("Empty gem - 10 sparks"), BazarBuy(NavigationGem(), 10)))
        choices.append((__("Leave"), 'leave'))
        choices.append((__("Sparks left: %s" % person.money), None))
        choice = renpy.display_menu(choices)
        if choice == 'leave':
            pass
        elif choice.item in worlds:
            person.money -= choice.price
            print(choice)
            gem = NavigationGem()
            gem.set_world(choice(core))
            person.add_item(gem)
        else:
            person.money -= choice.price
            person.add_item(choice)
    if choice != 'leave':
        call lbl_actions_bazar(action)
    return
