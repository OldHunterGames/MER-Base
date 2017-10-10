init python:
    wishes_data = {
        'wealth': {
            'name': __('Wealth'),

        },
        'vacation':{
            'name': __("Vacation")
        },
        'curiosity':{
            'name': __('Curiosity')
        },
        'agency':{
            'name': __('Agency')
        },
        'promotion':{
            'name': __('Promotion')
        },
        'fall_in_love':{
            'name': __('Fall in love')
        },
        'amity':{
            'name': __('Amity')
        },
        'ally':{
            'name': __('ally')
        },
        'power_struggle':{
            'name': __('Power struggle')
        },
        'reciprocity':{
            'name': __('Reciprocity')
        },
        'conflict':{
            'name': __('Conflict')
        },
        'loyality':{
            'name': __('Loyality')
        },
        'independence':{
            'name': __('Independence')
        },
        'atonement':{
            'name': __('Atonement')
        },
        'malice':{
            'name': __('Malice')
        },
        'agression':{
            'name': __('Agression')
        },
        'serenity':{
            'name': __('Serenity')
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

label lbl_wish_wealth_end(person):
    $ core.add_personal_record(person, "{person.full_name} focuses on business and gain additional cash.".format(person=person))
    $ person.add_resource('cash', 1)
    return

label lbl_wish_wealth_chance(person):
    return 5 - person.resource('cash') + person.need_level('prosperity')

label lbl_wish_vacation_end(person):
    $ core.add_personal_record(person, "{person.full_name} enjoying idleness.".format(person=person))
    return

label lbl_wish_vacation_chance(person):
    return 1 + person.need_level('comfort')

label lbl_wish_curiosity_end(person):
    $ core.add_personal_record(person, "{person.full_name} learned an important secret and has more information now.".format(person=person))
    $ person.add_resource('info', 1)
    return 

label lbl_wish_curiosity_chance(person):
    return 5 - person.resource('info') + person.need_level('communication')

label lbl_wish_agency_end(person):
    $ core.add_personal_record(person, "{person.full_name} considers some possibilities to gain more power.".format(person=person))
    $ person.add_resource('power', 1)
    return 

label lbl_wish_agency_chance(person):
    return 5 - person.resource('power') + person.need_level('authority')

label lbl_wish_promotion_end(person):
    python:
        resources = [key for key, value in person.resources().items() if value == 5]
        if any(resources):
            resource = random.choice(resources)
            person.use_resource(resource, 5)
        else:
            resource = None
        if person.occupation_level < person.occupation_attribute_value() and resource is not None:
            core.add_personal_record(person, "{person.full_name} leveled up as a {person.occupation_name}.".format(person=person))
            person.occupation_level += 1
        else:
            core.add_personal_record(person, "{person.full_name} can't get a progress as a {person.occupation_name} andd needs to blame someone.".format(person=person))
            core.wish_maker.reserve_wish(person, 'power_struggle')
    return

label lbl_wish_promotion_chance(person):
    if person.occupation_level == 5:
        return 0
    elif all([i < 5 for i in person.resources().values()]):
        return 0
    return 6 + person.need_level('ambitions') * 2

label lbl_wish_fall_in_love_end(person):
    python:
        # rework this after attraction mechanics is done
        persons = set()
        additional_persons = 3
        for i in core.get_active_persons(person):
            attraction = person.orientation_fit(i)
            if attraction > 0:
                if i.has_positive_bonds_with(person):
                    persons.add(i)
                elif additional_persons > 0:
                    persons.add(i)
                    additional_persons -= 1
        additional_persons += 1
        persons.update(make_phantoms(additional_persons))
        target = make_bond(person, 'lover', clear_targets(person, 'lover', persons))
        core.add_personal_record(person, "{person.full_name} fall in love with {target.full_name}.".format(person=person, target=target))

    return

label lbl_wish_fall_in_love_chance(person):
    python:
        value = person.need_level('eros')
        value += sum([1 for i in person.known_characters() if i.get_bond(person, 'lover') is not None])
        if 'ardent' in person.alignment():
            value += 1
        elif 'timid' in person.alignment():
            value -= 1
        if not person.has_bond('lover'):
            value += 3
    return value

label lbl_wish_amity_end(person):
    python:
        persons = set()
        additional_persons = 3
        for i in core.get_active_persons(person):
            attraction = person.orientation_fit(i)
            if attraction < 0:
                if i.has_positive_bonds_with(person):
                    persons.add(i)
                elif additional_persons > 0:
                    persons.add(i)
                    additional_persons -= 1
        additional_persons += 1
        persons.update(make_phantoms(additional_persons))
        target = make_bond(person, 'friend', clear_targets(person, 'friend', persons))
        core.add_personal_record(person, "{person.full_name} now considers {target.full_name} as a friend.".format(person=person, target=target))        
    return

label lbl_wish_amity_chance(person):
    python:
        value = 3
        value += person.need_level('comunication')
        value -= sum([1 for i in person.known_characters() if i.has_positive_bonds_with(person)])
        if 'good' in person.alignment():
            value += 1
        elif 'evil' in person.alignment():
            value -= 1
        if not person.has_bond('friend'):
            value += 1
    return value

label lbl_wish_ally_end(person):
    python:
        persons = set()
        additional_persons = 3
        for i in core.get_active_persons(person):
            our_bonds = person.has_bonds_with(i)
            target_bonds = i.has_positive_bonds_with(person)
            if not our_bonds and target_bonds:
                persons.add(i)
            elif additional_persons > 0:
                persons.add(i)
                additional_persons -= 1
        additional_persons += 1
        persons.update(make_phantoms(additional_persons))
        target = make_bond(person, 'ally', clear_targets(person, 'ally', persons))
        core.add_personal_record(person, "{person.full_name} makes alliance with {target.full_name}.".format(person=person, target=target))        
    return

label lbl_wish_ally_chance(person):
    python:
        value = 5
        value -= person.occupation_level
        value -= sum([1 for i in person.known_characters() if i.get_bond(person, 'ally') is not None])
        if 'lawful' in person.alignment():
            value += 1
        elif 'chaotic' in person.alignment():
            value -= 1
        if not person.has_bond('ally'):
            value += 3
    return value

label lbl_wish_power_struggle_end(person):
    python:
        persons = set()
        additional_persons = 3
        for i in core.get_active_persons(person):
            target_bonds = i.has_negative_bonds_with(person)
            if target_bonds:
                persons.add(i)
            elif additional_persons > 0 and i.occupation == person.occupation:
                persons.add(i)
                additional_persons -= 1
        persons.update(make_phantoms(1))
        target = make_bond(person, 'rival', clear_targets(person, 'rival', persons))
        core.add_personal_record(person, "{person.full_name} considers {target.full_name} as a rival.".format(person=person, target=target))        
    return

label lbl_wish_power_struggle_chance(person):
    return 0

label lbl_wish_reciprocity_end(person):
    python:
        persons = set()
        for i in person.known_characters():
            target_bonds = i.has_bonds_with(person)
            if target_bonds:
                persons.add(i)
        target = random.choice(list(persons))
        bond = target.get_bond_with(person)
        old_target = person.remove_bond_by_slot(bond.id)
        if old_target is not None:
            old_target.add_bond(Bond(person, 'traitor'))
        person.add_bond(Bond(target, bond.id))
    $ core.add_personal_record(person, "{person.full_name} reciprocates on {target.full_name} attitude.".format(person=person, target=target))
    return

label lbl_wish_reciprocity_chance(person):
    python:
        value = 0
        bonus = 1
        for i in ('good', 'lawful', 'timid'):
            if i in person.alignment():
                bonus -= 1
        for i in ('chaotic', 'ardent', 'evil'):
            if i in person.alignment():
                bonus += 1
        for i in person.known_characters():
            our_bond = person.has_bonds_with(i)
            target_bond = i.has_bonds_with(person)
            if not our_bond and target_bond:
                value += bonus
    
    return value

label lbl_wish_conflict_end(person):
    python:
        persons = set()
        additional_persons = 3
        for i in core.get_active_persons(person):
            target_bonds = i.has_negative_bonds_with(person)
            if not target_bonds and additional_persons > 0:
                persons.add(i)
        additional_persons += 1
        persons.update(make_phantoms(additional_persons))
        bond_id = random.choice([key for key, value in bonds_data.items() if value['value'] < 0])
        target = random.choice(list(persons))
        person.add_bond((Bond(target, bond_id)))
        core.add_personal_record(person, "{person.full_name} conflicts with {target.full_name}.".format(person=person, target=target))        
    return

label lbl_wish_conflict_chance(person):
    python:
        value = 3
    return value

label lbl_wish_loyality_end(person):
    python:
        bond = random.choice([i for i in person.get_bonds().values() if i.value > 0])
        bond.target.add_resource(random.choice(('power', 'info', 'cash')), person.occupation_level)
        bond.target.add_bond(Bond(person, bond.id))
        target = bond.target
        core.add_personal_record(person, "{person.full_name} helps {target.full_name} out of loyalty.".format(person=person, target=target))
    return

label lbl_wish_loyality_chance(person):
    python:
        value = 0
        value += sum([2 for i in person.get_bonds().values() if i.value > 0])
        if value > 0:
            if 'lawful' in person.alignment():
                value += 3
            elif 'chaotic' in person.alignment():
                value -= 3
    return value

label lbl_wish_independence_end(person):
    python:
        bond = random.choice([i for i in person.get_bonds().values()])
        target = bond.target
        person.remove_bond(bond)
    $ core.add_personal_record(person, "{person.full_name} is not interested in {target.full_name} anymore.".format(person=person, target=target))        
    return

label lbl_wish_independence_chance(person):
    python:
        value = 0
        value += sum([1 for i in person.get_bonds().values()])
        if value > 0:
            if 'chaotic' in person.alignment():
                value += 3
            elif 'lawful' in person.alignment():
                value -= 3
    return value

label lbl_wish_atonement_end(person):
    python:
        persons = set()
        for i in person.known_characters():
            bond = i.get_bond_with(person)
            if bond is not None:
                if bond.value < 0:
                    persons.add(i)
        target = random.choice(list(persons))
        target.remove_all_bonds_with(person)
        target.add_resource(random.choice(('power', 'cash', 'info')), person.occupation_level)
    $ core.add_personal_record(person, "{person.full_name} pays off for a grudge with a {target.full_name}".format(person=person, target=target))
    return

label lbl_wish_atonement_chance(person):
    python:
        value = 0
        value += sum([1 for i in person.known_characters() if i.has_negative_bonds_with(person)])
        if value > 0:
            if 'good' in person.alignment():
                value += 3
            elif 'evil' in person.alignment():
                value -= 3
    return value

label lbl_wish_malice_end(person):
    python:
        persons = set()
        for i in person.known_characters():
            our_bond = person.has_positive_bonds_with(i)
            target_bond = i.has_positive_bonds_with(person)
            if our_bond and target_bond:
                persons.add(i)
        target = random.choice(list(persons))
        person.remove_all_bonds_with(target)
        target.remove_all_bonds_with(person)
        target.add_bond(Bond(person, 'traitor'))
        person.add_resource(random.choice(('power', 'cash', 'info')), target.occupation_level)
    $ core.add_personal_record(person, "{person.full_name} betrays {target.full_name} feelings.".format(person=person, target=target))
    return

label lbl_wish_malice_chance(person):
    python:
        value = 0
        for i in person.known_characters():
            if i.has_positive_bonds_with(person) and person.has_positive_bonds_with(i):
                value += 3
        if value > 0:
            if 'evil' in person.alignment():
                value += 5
            elif 'good' in person.alignment():
                value -= 5
    return value

label lbl_wish_agression_end(person):
    python:
        persons = set()
        for i in person.get_bonds().values():
            if i.value < 0:
                persons.add(i.target)
        target = random.choice(list(persons))
        person.remove_all_bonds_with(target)
        for i in range(0, person.occupation_level):
            resources = [key for key, value in target.resources().items() if value > 0]
            try:
                resource = random.choice(resources)
                target.use_resource(resource, 1)
            except IndexError:
                target.occupation_level -= 1
                break
    $ core.add_personal_record(person, "{person.full_name} undermines {target.full_name} resources.".format(person=person, target=target))
    return

label lbl_wish_agression_chance(person):
    python:
        value = 0
        value += sum([2 for i in person.known_characters() if person.has_negative_bonds_with(i)])
        if value > 0:
            if 'ardent' in person.alignment():
                value += 3
            elif 'timid' in person.alignment():
                value -= 3
    return value

label lbl_wish_serenity_end(person):
    python:
        bonds = [i for i in person.get_bonds().values() if i.value < 0]
        bond = random.choice(bonds)
        target = bond.target
        person.remove_bond(bond)
    $ core.add_personal_record(person, "{person.full_name} ceases hostility towards the {target.full_name}.".format(person=person, target=target))
    return

label lbl_wish_serenity_chance(person):
    python:
        value = 0
        value += sum([2 for i in person.get_bonds().values() if i.value < 0])
        if value > 0:
            if 'ardent' in person.alignment():
                value += 3
            if 'timid' in person.alignment():
                value -= 3
    return value