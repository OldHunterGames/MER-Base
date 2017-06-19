init python:
    intrigues_data = {
        'assassination': 
            {
                'name': __("Assassination"), 
                'end_label': 'lbl_intrigue_assassination_end',
                'on_init_label': 'lbl_intrigue_assassination_on_init',
                'check_label': 'lbl_intrigue_assassination_check'
            }
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

label lbl_intrigue_assassination_check(intrigue):
    return True