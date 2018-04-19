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
    menu:
        'You see some native girls running into fores when you arrive'
        'Try to catch any girl':
            python:
                check = Skillcheck(world.player, 'hardiness', 2).run()
            if check:
                python:
                    girl = core.person_creator.gen_random_person(gender='female', age='junior')
                '[world.player.name] ran fast enough to catch [girl.age] girl'
            else:
                'You were to slow to catch anyone'

        'Try to lure any girl':
            python:
                check = Skillcheck(world.player, 'competence', 2).run()
            if check:
                python:
                    girl = core.person_creator.gen_random_person(gender='female', age='adolescent')
                '[world.player.name] were smart enough to lure [girl.age] girl'
            else:
                'You did not lure anyone'

    
    if check:
        python:
            world.player.enslave(girl)
            world.sync_world()
    return