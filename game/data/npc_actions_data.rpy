init python:
    npc_actions_data = {
        'vacation':{
            'name': __("Vacation"),
            'cls': VacationAction,
        },
        'promotion': {
            'name': __("Promotion"),
        }
    }

    def make_bond(person, bond_id, targets):
        target = random.choice(list(targets))
        person.add_bond(Bond(target, bond_id))
        return target

    def clear_targets(person, bond_id, targets):
        return [i for i in targets if person.get_bond(i, bond_id) is None]

    def make_phantoms(amount, filter=None):
        return [core.person_creator.gen_random_person() for i in range(0, amount)]


label lbl_npc_action_vacation_act(person, action):
    $ core.add_personal_record(person, "{person.full_name} enjoying idleness.".format(person=person))
    return

label lbl_npc_action_vacation_chance(person, action):
    return action.action_fatigue.get(person, 0)

label lbl_npc_action_promotion_act(person, action):
    python:
        occupation = Occupation.get_occupation(person)
        if occupation is not None:
            occupation.promote(person)
            person.ability = None
            core.add_personal_record(person, "{person.full_name} promotes in occupation".format(person=person))
    return

label lbl_npc_action_promotion_chance(person, action):
    python:
        occupation = Occupation.get_occupation(person)
    if occupation is None:
        return 0
    python:
        if occupation is not None:
            lvl = occupation.level(person)
    if person.ability is not None and person.ability.id == 'power' and lvl < 5:
        return 10
    return 0


