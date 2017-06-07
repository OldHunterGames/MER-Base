style char_info_window is window:
    background Color((0, 0, 0, 255))
    xfill True
    yfill True
    xsize 1280
    ysize 720
screen sc_cis(person, controlled=False, creation=False, relations=None):

    window:
        style 'char_info_window'
        hbox:
            vbox:
                image im.Scale(person.avatar, 200, 200)
                for key, value in person.show_stats().items():
                    text encolor_text(key, value)
            text DescriptionMaker(person).description(relations)
        if creation:
            use gen_button
        textbutton 'Items':
            xalign 0.6
            yalign 0.7
            action Show('sc_simple_equip', person=person)
        if controlled:
            textbutton 'Contacts':
                xalign 0.6
                yalign 0.8
                action Function(renpy.call_in_new_context, 'lbl_contacts', person)
        else:
            textbutton 'Leave':
                xalign 0.6
                yalign 0.8
                action Return()

screen gen_button():
    textbutton 'Generate':
        xalign 0.6
        yalign 0.6
        action Return()