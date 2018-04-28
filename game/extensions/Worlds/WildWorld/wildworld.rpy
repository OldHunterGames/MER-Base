init python:


    class WildWorld(World):
        type = 'Wild world'
        count = 1

        fatness_maping = {
            -2: 1,
            -1: 2,
            0: 4,
            1: 6,
            2: 10
        }

        BASIC_AP = 5

        def __init__(self, *args, **kwargs):
            super(WildWorld, self).__init__(*args, **kwargs)
            self.number = WildWorld.count
            self.food = 25
            self.ap = self.BASIC_AP
            self.captives = list()
            WildWorld.count += 1

        def food_consumption(self):
            return self.fatness_maping[self.player.fatness] + sum([self.fatness_maping[i.fantess] for i in self.captives])

        def entry_point(self):
            return 'lbl_wildworld'
    
        def name(self):
            return '{0} {1}'.format(self.type, self.number)

        def get_path(self):
            return 'WildWorld/resources/'

        def capture(self, person):
            self.capture.append(person)
            self.player.enslave(person)

        def skip_turn(self):
            self.food -= self.food_consumption()
            if self.food < 0:
                self.food = 0
                self.starving_points += 1
            else:
                self.starving_points = 0
            self.ap = self.BASIC_AP - abs(self.starving_points)
            renpy.call_in_new_context('lbl_wildworld_starvation', world=self)

        def attributes(self, person):
            attrs = []
            for key, value in person.raw_attributes().items():
                attrs.append(self.path('img/stats/' + '{0}_{1}.png'.format(key, value)))
            return attrs

label lbl_wildworld(world):
    $ name = world.name()
    $ world.captive = list()
    'Wellcome to [name]'
    show expression im.Scale(world.path('img/entry.jpg'), 1280, 720) as wirldworld_entry
    show screen sc_wildworld_stats(world)
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


label lbl_wildworld_starvation(world):
    'You are starving'
    return