init python:


    class WildWorld(World):
        type = 'Wild world'
        count = 1

        def __init__(self, *args, **kwargs):
            super(WildWorld, self).__init__(*args, **kwargs)
            self.number = WildWorld.count
            WildWorld.count += 1

        def entry_point(self):
            return 'lbl_wildworld'
    
        def name(self):
            return '{0} {1}'.format(self.type, self.number)


label lbl_wildworld(world):
    $ name = world.name()
    'Wellcome to [name]'
    return