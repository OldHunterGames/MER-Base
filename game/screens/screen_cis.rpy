style char_info_window is window:
    background Color((0, 0, 0, 255))
screen sc_cis(person):

    window:
        xfill True
        yfill True
        xsize 1280
        ysize 720
        style 'char_info_window'
        hbox:
            vbox:
                image im.Scale(person.avatar, 200, 200)
                for key, value in person.show_stats().items():
                    text encolor_text(key, value)
            text DescriptionMaker(person).description()
        use gen_button

screen gen_button():
    textbutton 'Generate':
        xalign 0.6
        yalign 0.6
        action Return()