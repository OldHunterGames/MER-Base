init python:
    interactions_data = {
        'give_money': {
            'name': __("Give money"),
            'descriptions': __("Gives money")
        }
    }

label lbl_interaction_give_money(source, actor):
    python:
        actor.money += 100
    '[source.name] gives some money to [actor.name]'
    return