screen sc_player_journal():
    window:
        style 'char_info_window'

        viewport:
            scrollbars 'vertical'
            draggable True
            mousewheel True
            ymaximum 700
            xmaximum 1000
            vbox:
                ymaximum 700
                xmaximum 1000
                spacing 5
                box_wrap True
                
                for i in core.get_records():
                    text i:
                        layout 'greedy'

        textbutton 'Leave':
            action Hide('sc_player_journal')
            xalign 1.0
            yalign 1.0