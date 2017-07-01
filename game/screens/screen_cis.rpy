style char_info_window is window:
    background Color((0, 0, 0, 255))
    xfill True
    yfill True
    xsize 1280
    ysize 720

label lbl_cis_glue(person, controlled=False, creation=False, relations=None):
    call screen sc_cis(person, controlled, creation, relations)
    return
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
        textbutton 'Schedule':
            xalign 0.6
            yalign 0.4
            action ShowTransient('sc_schedule', person=person)
        if person.has_intrigue():
            textbutton 'Intrigue':
                action Show('sc_intrigue_info', person=person)
                xalign 0.6
                yalign 0.6
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
    on 'hide':
        action Hide('sc_intrigue_info')

screen sc_intrigue_info(person):
    window:
        vbox:
            text 'Intrigue name: ' + person.intrigue.name
            hbox:
                vbox:
                    text 'Intigue target: '
                    text person.intrigue.target.name
                imagebutton:
                    idle im.Scale(person.intrigue.target.avatar, 50, 50)
                    action Function(renpy.call_in_new_context, 'lbl_cis_glue', person=person.intrigue.target, relations=player)
            textbutton 'Close' action Hide('sc_intrigue_info')
            textbutton 'End intrigue':
                action Hide('sc_intrigue_info'), Function(person.end_intrigue)

screen gen_button():
    textbutton 'Generate':
        xalign 0.6
        yalign 0.6
        action Return()

    textbutton 'Random faction':
        xalign 0.6
        yalign 0.5
        action Function(renpy.call_in_new_context, 'show_random_faction')