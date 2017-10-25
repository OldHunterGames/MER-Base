
style char_info_window is window:
    background Color((0, 0, 0, 255))
    xfill True
    yfill True
    xsize 1280
    ysize 720

label lbl_cis_glue(person, controlled=False, relations=None):
    call screen sc_cis(person, controlled, relations)
    return


label lbl_new_meeting(person):
    $ new_person = core.person_creator.gen_random_person()
    $ person.relations(new_person)
    $ core.faction.add_member(new_person)
    return

screen sc_cis(person, controlled=False, relations=None):

    window:
        style 'char_info_window'
        hbox:
            vbox:
                image im.Scale(person.avatar, 200, 200)
                
            text DescriptionMaker(person).description(relations)

        vbox:
            ypos 201
            for key, value in person.show_attributes().items():
                text encolor_text(key, value)
            if not controlled:
                for key, value in person.show_resources().items():
                    text '%s: %s' % (key.capitalize(), value)
            if controlled:
                text 'Money: %s'%person.money
            for i in DescriptionMaker(person).bonds_text():
                text i
        
        # textbutton 'Items':
        #     xalign 0.6
        #     yalign 0.7
        #     action Show('sc_simple_equip', person=person)
        if controlled:
            textbutton 'Schedule':
                xalign 0.6
                yalign 0.4
                action ShowTransient('sc_schedule', person=person)

            textbutton 'Motivations':
                xalign 0.6
                yalign 0.6
                action Function(CardMenu((SeeCard(i) for i in person.get_motivations()), cancel=True).show)

            textbutton 'Conditions':
                xalign 0.6
                yalign 0.7
                action Function(CardMenu((SeeCard(i) for i in person.get_conditions()), cancel=True).show)
            textbutton 'House':
                xalign 0.8
                yalign 0.8
                action ShowTransient('sc_pick_house', person=person)
            textbutton 'New meeting':
                xalign 0.6
                yalign 0.5
                action Function(renpy.call_in_new_context, 'lbl_new_meeting', person=person)
            textbutton 'Contacts':
                xalign 0.6
                yalign 0.8
                action Function(renpy.call_in_new_context, 'lbl_contacts', person)
            textbutton 'Skip turn':
                xalign 1.0
                yalign 1.0
                action Function(core.skip_turn), SensitiveIf(core.can_skip_turn())
                hovered If(not core.can_skip_turn(), ShowTransient('sc_text_popup', text='You have no money'))
                unhovered Hide('sc_text_popup')
            textbutton 'Journal':
                xalign 0.8
                yalign 0.6
                action Show('sc_journal', None, core.get_records())
        
        else:
            textbutton 'Leave':
                xalign 0.6
                yalign 0.8
                action Return()
            textbutton 'Journal':
                xalign 0.8
                yalign 0.6
                action Show('sc_journal', None, core.get_personal_records(person))

    on 'hide':
        action Hide('sc_intrigue_info')

screen sc_gen_player():
    $ person = core.player
    window:
        style 'char_info_window'
        hbox:
            vbox:
                image im.Scale(person.avatar, 200, 200)
                for key, value in person.show_attributes().items():
                    text encolor_text(key, value)
            text DescriptionMaker(person).description(None)
        textbutton 'Generate':
            xalign 0.6
            yalign 0.6
            action Function(core.create_player)

        textbutton 'Start':
            xalign 0.6
            yalign 0.5
            action Return()
