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
        return die_callback

label lbl_intrigue_assassination_on_init(intrigue):
    $ intrigue.target.die.add_callback(assassination_callback(intrigue))
    return

label lbl_intrigue_assassination_end(intrigue):
    '[intrigue.name] ended'
    return

label lbl_intrigue_assassination_check(intrigue):
    return True