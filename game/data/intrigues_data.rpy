init python:
    intrigues_data = {
        'assassination': 
            {
                'name': __("Assassination"), 
            },

        'befriend': 
            {
                'name': __("Befriend"), 
            },

        'seduction':
            {
                'name': __("Seduction"),
            },

        'harassment':
            {
                'name': __("Harassment"),
            },
        'support':
            {
                'name': __("Support"),
            },

        'breakup':
            {
                'name': __("Breakup"),
            },

        'vendetta':
            {
                'name': __("Vendetta"),
            },

        'recruitment':
            {
                'name': __("Recruitment"),
            },

        'submission':
            {
                'name': __("Submission"),
            },

    }

label lbl_intrigue_assassination_check(intrigue):
    return True

label lbl_intrigue_assassination_intervene(intrigue):
    'intervened'
    return

label lbl_intrigue_assassination_end(intrigue):
    if not intrigue.target.is_dead():
        $ intrigue.target.die.remove_callback(intrigue.callback)
        $ intrigue.target.die()
    $ core.add_record('[intrigue.name] ended')
    show expression im.Scale(intrigue.target.avatar, 200, 200) at truecenter
    $ core.add_record("[intrigue.target.name] is dead")
    return

label lbl_intrigue_befriend_check(intrigue):
    if 'evil' in intrigue.target.alignment():
        return False
    return True


label lbl_intrigue_befriend_end(intrigue):
    if intrigue.initiator.charisma() > intrigue.target.charisma():
        python:
            bond = Bond(intrigue.target, 'friend')
            intrigue.initiator.add_bond(bond)
            bond = Bond(intrigue.initiator, 'friend')
            intrigue.target.add_bond(bond)
        $ core.add_record('[intrigue.initiator.name] befriended [intrigue.target.name]')
    else:
        python:        
            bond = Bond(intrigue.target, 'rejected')
            intrigue.initiator.add_bond(bond)
        $ core.add_record('[intrigue.target.name] rejected [intrigue.initiator.name]')
    return

label lbl_intrigue_seduction_check(intrigue):
    $ attraction = True #should be attraction check
    return attraction

label lbl_intrigue_seduction_end(intrigue):
    $ check = True #should be success check
    if check:
        $ intrigue.target.add_bond(Bond(intrigue.initiator, 'lover'))
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'lover'))
        $ core.add_record('[intrigue.initiator.name] seduced [intrigue.target.name]')
    else:
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'rejected'))
        $ core.add_record('[intrigue.target.name] rejected [intrigue.initiator.name] seducation')
    return

label lbl_intrigue_harassment_check(intrigue):
    return 'timid' not in intrigue.initiator.alignment()

label lbl_intrigue_harassment_end(intrigue):
    $ check = True #should be success check
    if check:
        $ intrigue.target.add_bond(Bond(intrigue.initiator, 'humiliated'))
        $ core.add_record('[intrigue.target.name] humiliated by [intrigue.initiator.name]')
    else:
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'humiliated'))
        $ core.add_record('[intrigue.initiator.name] humiliated by [intrigue.target.name]')
    return

label lbl_intrigue_support_check(intrigue):
    return 'ardent' not in intrigue.initiator.alignment()

label lbl_intrigue_support_end(intrigue):
    $ check = True #should be success check
    if check:
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'supporter'))
        $ core.add_record('[intrigue.initiator.name] is now supporter of [intrigue.target.name]')
    else:
        $ intrigue.target.add_bond(Bond(intrigue.initiator, 'supporter'))
        $ core.add_record('[intrigue.target.name] is now supporter of [intrigue.initiator.name]')

    return

label lbl_intrigue_breakup_check(intrigue):
    return ('lawful' not in intrigue.initiator.alignment() and 
        any(intrigue.initiator.get_bonds_with(intrigue.target)))

label lbl_intrigue_breakup_end(intrigue):
    python:
        for i in intrigue.initiator.get_bonds_with(intrigue.target):
            intrigue.initiator.remove_bond(i)
        for i in intrigue.target.get_bond_with(intrigue.initiator):
            intrigue.target.remove_bond(i)
        check = True # should be success check
    if check:
        $ intrigue.target.add_bond(Bond(intrigue.initiator, 'rejected'))
        $ core.add_record('[intrigue.initiator.name] broke with [intrigue.target.name]')
    else:
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'rejected'))
        $ core.add_record('[intrigue.target.name] broke with [intrigue.initiator.name]')
    return

label lbl_intrigue_vendetta_check(intrigue):
    python:
        others = [i for i in intrigue.initiator.known_characters()
            if intrigue.initiator.has_positive_bonds_with(i)]
        love_triangle_check = any([intrigue.target.has_bonds_with(i) for i in others])
        if love_triangle_check:
            intrigue.other = random.choice(others)
        alignment_check = 'chaotic' not in intrigue.initiator.alignment()
    
    return alignment_check and love_triangle_check

label lbl_intrigue_vendetta_end(intrigue):
    $ check = True # should be success check
    if check:
        python:
            intrigue.target.remove_all_bonds_with(intrigue.other)
            intrigue.other.remove_all_bonds_with(intrigue.target)
            intrigue.target.add_bond(Bond(intrigue.initiator, 'humiliated'))
            core.add_record('[intrigue.initiator.name] successfully commited a vendetta over [intrigue.target.name]')
    else:
        python:
            intrigue.initiator.remove_all_bonds_with(intrigue.target)
            intrigue.target.remove_all_bonds_with(intrigue.initiator)
            intrigue.initiator.add_bond(Bond(intrigue.target, 'humiliated'))
            core.add_record('[intrigue.initiatore.name] failed vendetta over [intrigue.target.name]')

    return


label lbl_intrigue_recruitment_check(intrigue):
    $ faction = intrigue.initiator.faction
    return faction.get_influence(intrigue.initiator) > faction.get_influence(intrigue.target)

label lbl_intrigue_recruitment_end(intrigue):
    $ check = True # should be success check
    if check:
        $ intrigue.target.add_bond(Bond(intrigue.initiator, 'mentor'))
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'underling'))
        $ core.add_record('[intrigue.initiator.name] successfully recruited [intrigue.target.name]')

    else:
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'rejected'))
        $ core.add_record('[intrigue.initiator.name] failed recruitment of [intrigue.target.name]')

    return

label lbl_intrigue_submission_check(intrigue):
    $ faction = intrigue.initiator.faction
    return faction.get_influence(intrigue.initiator) < faction.get_influence(intrigue.target)

label lbl_intrigue_submission_end(intrigue):
    $ check = True # should be success check
    if check:
        $ intrigue.target.add_bond(Bond(intrigue.initiator, 'underling'))
        $ core.add_record('[intrigue.initiator.name] submissed [intrigue.target.name]')
    else:
        $ intrigue.initiator.add_bond(Bond(intrigue.target, 'rejected'))
        $ core.add_record('[intrigue.initiator.name] failed submission of [intrigue.target.name]')

    return