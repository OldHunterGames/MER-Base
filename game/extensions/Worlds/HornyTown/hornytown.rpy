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

label ow_hornytown_enter(world):
    screen black
    $ name = world.name()
    'Wellcome to [name]'

    call ow_hornytown_gt(world)
    return

label ow_hornytown_gt(world):
    show bg road
    '...'

    return
