init python:

    abilities_data = {
        'wealth': {
            'name': __("Wealth"),
            'description': __("Have some extra Sparks to spend"),
            'interactions': [],
        },
        'bankrupt': {
            'name': __("Bankrupt"),
            'description': __("Have serious financial dificulities that may lead to debt-enslavement"),
            'interactions': [],
            'on_add': 'lbl_ability_bankrupt_add'
        },
        'power': {
            'name': __("Power"),
            'description': __("Have a considerable personal power within a faction"),
            'interactions': [],
        },
        'weaken': {
            'name': __("Weaken"),
            'description': __("Severly weaken in a recent struggle and in a danger of death if attacked. All contests are done with penalty"),
            'modifiers': {'skillcheck': -1}
        },
        'info': {
            'name': __("Info"),
            'description': __("Knows some major secret"),

        },
        'humiliated': {
            'name': __("Humiliated"),
            'description': __("Was humiliated in the eyes of the faction and so will not get help from allies, lovers and friends. Is in danger of excommunication")
        }
    }

label lbl_ability_bankrupt_add(person, ability, prev_ability):
    if ability == prev_ability:
        'Person [person.name] will sell his slave or become slave'
    return
