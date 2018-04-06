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
        }
    }

label lbl_ability_bankrupt_add(person, ability, prev_ability):
    if ability == prev_ability:
        'Person [person.name] will sell his slave or become slave'
    return
