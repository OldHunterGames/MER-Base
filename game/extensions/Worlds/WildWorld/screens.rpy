screen sc_wildworld_stats(world):
    
    window:
        background Color((0, 0, 0, 100))
        xfill True
        yfill True
        ysize 720
        xsize 192
        xpos 1168

        vbox:
            spacing 10
            xalign 0.5
            xsize 180
            image im.Scale(world.player.avatar, 180, 180):
                xalign 0.5
            hbox:
                for i in world.attributes(world.player):
                    image i
                spacing 2
                xalign 0.5
            hbox:
                image world.path('img/ham-shank.png')
                text '%s' % world.food:
                    yalign 0.5
                spacing 5
            hbox:
                image world.path('img/eating.png')
                text '%s' % world.food_consumption():
                    yalign 0.5
                spacing 5
            for key, value in world.player.show_attributes().items():
                text encolor_text(key, value)
            image Borders(1,1,1,1)
            imagebutton:
                if len(world.captives) > 0:
                    idle world.path('img/imprisoned.png')
                else:
                    idle world.path('img/imprisoned_inactive.png')
                hover world.path('img/imprisoned_hover.png')
                sensitive len(world.captives) > 0
                # hovered Show('sc_text_popup', text='See your captives')
                # unhovered Hide('sc_text_popup')
                action NullAction()

            $ tooltip = GetTooltip()

            if tooltip:
                text '[tooltip]'
                


