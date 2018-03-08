init python:


    class Goldriver(World):
        type = 'Gold River'
        count = 1

        def __init__(self, *args, **kwargs):
            super(Goldriver, self).__init__(*args, **kwargs)
            self.number = Goldriver.count
            Goldriver.count += 1
            self.ingot = True
            self.gold = 0

        def entry_point(self):
            return 'ow_goldriver_enter'

        def name(self):
            return '{0} {1}'.format(self.type, self.number)
