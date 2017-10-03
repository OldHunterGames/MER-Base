screen sc_journal(records_list, called=False):
    modal True
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
                
                for i in records_list:
                    text i

        textbutton 'Leave':
            action If(called, Return(), false=Hide('sc_journal'))
            xalign 1.0
            yalign 1.0