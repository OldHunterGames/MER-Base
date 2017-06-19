init python:

    def avatar_with_intrigue(person):
        if person.has_intrigue():
            size = (200, 200)
            return LiveComposite(size,
                (0, 0), im.Scale(person.avatar, 200, 200),
                (150, 150), im.Scale('gui/vosk-zn-6.png', 50, 50))
        else:
            return im.Scale(person.avatar, 200, 200)

    def make_intrigues(faction, player):
        members = faction.get_members()
        random.shuffle(members)
        intrigues_made = 0
        for i in members:
            if i.has_intrigue():
                continue
            result = _make_intrigue(faction, i, player)
            if result:
                intrigues_made += 1
            if intrigues_made >= faction.max_intrigues:
                return

    def _make_intrigue(faction, person, player):
        members = faction.get_members()
        random.shuffle(members)
        for i in members:
            if i != person:
                return _get_intrigue(person, i, player)
    
    def _get_intrigue(initiator, target, player):
        for i in store.intrigues_data:
            intrigue = Intrigue(i, initiator, target, player)
            if intrigue.is_available():
                initiator.set_intrigue(intrigue)
                return True
        return False


screen sc_faction(faction):
    python:
        members = faction.get_members()
    window:
        style 'char_info_window'
        frame:
            xalign 0.5
            background faction.get_frame_color(members[0])
            imagebutton:
                idle avatar_with_intrigue(members[0])
                action Function(renpy.call_in_new_context, 'lbl_cis_glue', person=members[0], relations=player)
        hbox:
            spacing 10
            for i in members[1:3]:
                frame:
                    background faction.get_frame_color(i)
                    imagebutton:
                        idle avatar_with_intrigue(i)
                        action Function(renpy.call_in_new_context, 'lbl_cis_glue', person=i, relations=player)
        hbox:
            spacing 10
            xalign 1.0
            for i in members[3:5]:
                frame:
                    background faction.get_frame_color(i)
                    imagebutton:
                        idle avatar_with_intrigue(i)
                        action Function(renpy.call_in_new_context, 'lbl_cis_glue', person=i, relations=player)

        textbutton 'Leave':
            yalign 0.35
            xalign 0.5
            action Return()
        textbutton 'Roll intrigues':
            yalign 0.40
            xalign 0.5
            action Function(make_intrigues, faction, player), SensitiveIf(
                    not all([i.has_intrigue() for i in faction.get_members()]))
        hbox:
            box_wrap True
            spacing 15
            yalign 1.0
            xalign 0.5
            for i in members[5:]:
                frame:
                    background faction.get_frame_color(i)
                    imagebutton:
                        idle avatar_with_intrigue(i)
                        action Function(renpy.call_in_new_context, 'lbl_cis_glue', person=i, relations=player)