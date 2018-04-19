init python:

    class SellMenu(CardMenu):

        def run(self, card):
            self.current_card = None
            self._cards_list.remove(card)
            return card.run()

label _lbl_card_menu(card_menu, called=True, x_size=200, y_size=300, spacing_=5, cancel=False):
    call screen sc_card_menu(card_menu, called, x_size, y_size, spacing_, cancel)
    return


screen sc_card_menu(card_menu, called=True, x_size=200, y_size=300, spacing_=5, cancel=False):
    modal True
    python:
        cards_in_table = 4
        cards = card_menu.get_sorted()
        cards_splitted = []
        while len(cards) / cards_in_table >= 1:
            cards_splitted.append(cards[cards_in_table-4:cards_in_table])
            cards_in_table += 4
        cards_splitted.append(cards[cards_in_table-4:cards_in_table])
        card_menu.called = called
    window:
        xfill True
        yfill True
        xsize 1280
        ysize 720
        style 'char_info_window'

        viewport:
            scrollbars 'vertical'
            draggable True
            mousewheel True
            xmaximum 880
            vbox:
                for cards_list in cards_splitted:
                    hbox:
                        xmaximum 880
                        spacing spacing_
                        for i in cards_list:
                            vbox:
                                xsize x_size
                                imagebutton:
                                    idle im.Scale(i.image(), x_size, y_size)
                                    action Function(card_menu.set_card, i)
                                text i.name():
                                    xalign 0.5
                    text ''
                if cancel:
                    imagebutton:
                        idle im.Scale(card_back(), x_size, y_size)
                        action [Function(card_menu.cancel_pick), If(called, Return(), false=Hide('sc_card_menu'))]
        if card_menu.current_card is not None:
            python:
                img = card_menu.current_card.image()
                txt = card_menu.current_card.description()
                if card_menu.current_card.is_active():
                    act = Function(card_menu.run)
                else:
                    txt = encolor_text(card_menu.current_card.inactive_hint(), 'red') + '\n' + txt
                    img = im.Grayscale(img)
                    act = NullAction()
            vbox:
                xpos 900
                xsize 380
                box_wrap False
                imagebutton:
                    idle im.Scale(img, x_size+100, y_size+100)
                    action act
                            
                    xalign 0.5
                viewport:
                    scrollbars 'vertical'
                    draggable True
                    mousewheel True
                    xmaximum 380
                    vbox:
                        xalign 0.5
                        if card_menu.current_card.has_additional_info():
                            textbutton 'Additional info':
                                action Function(card_menu.current_card.additional_info)
                        text txt:
                            xmaximum 380