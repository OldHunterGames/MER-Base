init python:


    class HornyTown(World):
        type = 'Horny Town'
        count = 1

        def __init__(self, *args, **kwargs):
            super(HornyTown, self).__init__(*args, **kwargs)
            self.number = HornyTown.count
            HornyTown.count += 1

        def entry_point(self):
            return 'ow_hornytown_enter'

        def name(self):
            return '{0} {1}'.format(self.type, self.number)

image bg road = 'extensions/Worlds/HornyTown/images/bg_road.png'
image bg street = 'extensions/Worlds/HornyTown/images/bg_street.png'
image bg pawnshop = 'extensions/Worlds/HornyTown/images/bg_pawnshop.png'

image man = 'extensions/Worlds/HornyTown/images/man.png'
image woman = 'extensions/Worlds/HornyTown/images/woman.png'

define pawner = Character('Pawn shop owner', color="#c8ffc8")
define pl = Character('You', color="#f8cfc8")

label ow_hornytown_enter(world):
    screen black
    $ name = world.name()
    'Wellcome to [name]'

    call ow_hornytown_gt(world)
    return

label ow_hornytown_gt(world):
    show bg road with dissolve
    'The Edge of Mists is right here. You also see a road leading to the town.'

    menu:
        'To the town':
            call ow_hornytown_street(world)

        'Return to the Mists':
            'You leaving the Outer World'

    return

label ow_hornytown_street(world):
    show bg street with dissolve
    "This is a main street of the town."
    menu:
        "Shoping district":
            "There is a pawn shop here."
            menu:
                "Pawn shop":
                    call ow_hornytown_pawnshop(world)
                "Leave":
                    call ow_hornytown_gt(world)
        "Edge of Mists":
            call ow_hornytown_gt(world)

    return

label ow_hornytown_pawnshop(world):
    show bg pawnshop with dissolve
    "When you entering the shop the bell on a dor rings."
    "The owner arrives from the back room."
    show man with moveinright
    pawner "What do you whant?"
    pl "I'm leaving already"

    hide man with moveoutleft
    call ow_hornytown_street(world)

    return
