init python:

    def avatar_with_intrigue(person):
        if person.has_intrigue():
            print(person)
            size = (200, 200)
            return LiveComposite(size,
                (0, 0), im.Scale(person.avatar, 200, 200),
                (150, 150), im.Scale('gui/vosk-zn-6.png', 50, 50))
        else:
            return im.Scale(person.avatar, 200, 200)


screen sc_faction(faction):
    python:
        members = faction.get_members()
    window:
        style 'char_info_window'
        frame:
            xalign 0.5
            background faction.get_frame_color(members[0])
            image avatar_with_intrigue(members[0])
        hbox:
            spacing 10
            for i in members[1:3]:
                frame:
                    background faction.get_frame_color(i)
                    image avatar_with_intrigue(i)
        hbox:
            spacing 10
            xalign 1.0
            for i in members[3:5]:
                frame:
                    background faction.get_frame_color(i)
                    image avatar_with_intrigue(i)

        textbutton 'Leave':
            yalign 0.35
            xalign 0.5
            action Return()
        hbox:
            box_wrap True
            spacing 15
            yalign 1.0
            xalign 0.5
            for i in members[5:]:
                frame:
                    background faction.get_frame_color(i)
                    image avatar_with_intrigue(i)