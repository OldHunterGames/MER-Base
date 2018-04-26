screen sc_wildworld_stats(world):
    
    window:
        background Color((0, 0, 0, 100))
        xfill True
        yfill True
        ysize 720
        xsize 180
        xpos 1180

        vbox:
            spacing 10
            xalign 0.5
            xsize 180
            image im.Scale(world.player.avatar, 150, 150):
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
            textbutton 'girls':
                action NullAction()


