init python:
    intrigues_data = {
        'assassination': 
            {
                'name': __("Assassination"), 
                'end_label': 'lbl_intrigue_assassination_end',
                'on_init_label': 'lbl_intrigue_assassination_on_init',
                'check_label': 'lbl_intrigue_assassination_check'
            },
        
#        'seduction'            
#            {
#                'name': __("Seduction"), 
#                'end_label': 'lbl_intrigue_seduction_end',
#                'on_init_label': 'lbl_intrigue_seduction_on_init',
#                'check_label': 'lbl_intrigue_seduction_check'
#            },

        'befriend': 
            {
                'name': __("Befriend"), 
                'end_label': 'lbl_intrigue_befriend_end',
                'on_init_label': None,
                'check_label': 'lbl_intrigue_befriend_check'
            },

    }

    def assassination_callback(intrigue):
        def die_callback(target, *args):
            reason = args[1].get('reason')
            if reason == intrigue.player:
                intrigue.player_influence = True
            target.die.remove_callback(die_callback)
            intrigue.initiator.end_intrigue()
        intrigue.callback = die_callback
        return die_callback

label lbl_intrigue_assassination_check(intrigue):
    return True

label lbl_intrigue_assassination_on_init(intrigue):
    $ intrigue.target.die.add_callback(assassination_callback(intrigue))
    return

label lbl_intrigue_assassination_end(intrigue):
    if not intrigue.target.is_dead():
        $ intrigue.target.die.remove_callback(intrigue.callback)
        $ intrigue.target.die()
    '[intrigue.name] ended'
    show expression im.Scale(intrigue.target.avatar, 200, 200) at truecenter
    "[intrigue.target.name] is dead"
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
        '[intrigue.initiator.name] befriended [intrigue.target.name]'
    else:
        python:        
            bond = Bond(intrigue.target, 'rejected')
            intrigue.initiator.add_bond(bond)
        '[intrigue.target.name] rejected [intrigue.initiator.name]'
    return

