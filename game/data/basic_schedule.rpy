init python:

    basic_jobs = {
        'idle': 
            {
                'name': __('Idle'), 
                'description': 'Idle\nJust rest and take your time for yourself.\n(Timid deed. Well rested - gain green action card.  Stagnation tenses your ambitions)', 
                # 'attribute': 'hardiness',
                'world': None,
                'image': 'miscards',
                'slot': 'job'
            },
        'trainer':
             {
                 'name': __('Slave trainer'),
                 'description': 'Train slaves. \nWork in the Guild as a hired slave trainer. \nWillpower based. \nLawful deed. \nSupremacy over slaves give you minor authority satisfaction. \nThis work is gloomy, with no amusement.',
                 'attribute': 'willpower',
                 'world': 'core',
                 'image': 'miscards',
                 'slot': 'job'
             },
        'mist_travel':
            {
                'name': __("Mist travel"),
                'description': 'Travels into mist',
                'world': 'core',
                'image': 'miscards',
                'slot': 'job'
            }
    }



    basic_accommodations = {
        'appartment': 
            {
            "name": __("Appartments"),
            'description': __("Standart apartments"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'unsheltered':
            {
            "name": __("Unsheltered (0)"),
            "description": __("Live on the streets"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'camping': 
            {
            "name": __("Camping"), 
            'description': __("Camp in the wilds"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'confined': 
            {
            "name": __("Confined"), 
            'description': __("Confined in a dungeon"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'cold_floor': 
            {
            "name": __("Cold floor"), 
            'description': __("Sleeps on a cold floor"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'cot_and_blanket': 
            {
            "name": __("Cot & Blanket"), 
            'description': __("Sleeps in a crouded room"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'comfortable_bed': 
            {
            "name": __("Comfortable bed"), 
            'description': __("Nice bed to sleep."),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'private_bedroom': 
            {
            "name": __("Private bedroom"), 
            'description': __("Owns a private bedroom"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
        'love_nest': 
            {
            "name": __("Love nest"), 
            'description': __("Huge bed to sleep with a concubine"),
            'cost': 0,
            'world': 'core',
            'slot': 'accommodation'
            },
    }

    basic_rations = {
        'famish': 
            {
            "name": __("Famish"),
            'description': __("Eat what you can get for free (basicaly nothing)."), 
            'cost': 0, 
            'world': 'core',
            'slot': 'ration'
            },
        'dry_half':
            {
                "name": __("Dry food (1)"),
                'description': __('Small portion of sublimated "slave-food". Costs 1 spark/decade.'),
                'cost': 1,
                'world': 'core',
                'slot': 'ration'
            },
        'dry':
            {
                "name": __("Dry food (3)"),
                'description': __('Standard portion of sublimated "slave-food". Costs 3 spark/decade.'),
                'cost': 3,
                'world': 'core',
                'slot': 'ration'
            },
        'dry_double':
            {
                "name": __("Dry food (5)"),
                'description': __('Double portion of sublimated "slave-food". Costs 5 spark/decade.'),
                'cost': 5,
                'world': 'core',
                'slot': 'ration'
            },
        'canned_half':
            {
            "name": __("Canned food (5)"), 
            'description': __("Small portion of canned food. Costs 5 sparks/decade."),
            'cost': 5, 
            'world': 'core',
            'slot': 'ration'
            },
        'canned': 
            {
            "name": __("Canned food (10)"), 
            'description': __("Standard portion of canned food. Costs 10 sparks/decade"),
            'cost': 10, 
            'world': 'core',
            'slot': 'ration'
            },
        'canned_double': 
            {
            "name": __("Canned food (20)"),
            'description': __("Double portion of canned food. Costs 20 sparks/decade"),
            'cost': 20, 
            'world': 'core',
            'slot': 'ration'
            },
        'cooked': 
            {
            "name": __("Pub food (25)"),
            'description': __("Eat cooked food in a local pub. It's good enough to give a minor taste pleasure but costs 25 sparks/decade"),
            'cost': 25,
            'world': 'core',
            'slot': 'ration'
            },
    }

    basic_extras = {
        'promenade': 
            {
            "name": __("Promenade"),
            'description': __("Long and thoughtful walks through the most beautiful places of the White City. (Minor entertainment. But it's free!)"), 
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'relax': 
            {
            "name": __("Relax"),
            'description': __("Jut take some time for a nap and make the world wait for you. (Get the pleasure of comfort.)"),
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'workout': 
            {
            "name": __("Workout"),
            'description': __("Workout persistently to maintain a tonus and excellent physical shape. (Get some adrenaline. It is good for your body.)"), 
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },            
        'thuglife': 
            {
            "name": __("Thug life"),
            'description': __("Abuse those who are weak and mock those who can't repel you. (Evil deed. Subtlety check. Feeling power satisfies your authority needs.)"),
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'flirt':
            {
            "name": __("Flirt"),
            'description': __("Do some meaningless flirtations with a strangers. (Interaction is good to satisfy communication needs, but makes your erotic desires burn.)"),
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'forum': 
            {
            "name": __("Forum"),
            'description': __("Hot philosophical and political discussions on the forum give an excellent lesson for a keen mind. (Competence check. Some interaction and minor feel of power.)"),
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'perform': 
            {
            "name": __("Perform"),
            'description': __("You will sing, dance or recite poetry. It does not matter. The main thing is to attract the awed attention of the crowd! (Ardent deed. Extravagance check. Get decent attention and minor achievement, but public attention can be dangerous!)"),
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'library': 
            {
            "name": __("Library (5)"), 
            'description': __("The Grand Library of Vatican is opened to everyone... for a fee. (5 sparks / decade. Enjoy some serenity and amusement, but your body will get stiff.)"),
            'cost': 5,
            'world': 'core',
            'slot': 'extra'
            },
        'tippling': 
            {
            "name": __("Tippling (10)"),
            'description': __("Drink at the pub, chat with patrons, paw maids. (10 sparks / decade. Minor amusement and some communication.)"),
            'cost': 0, 
            'world': 'core',
            'slot': 'extra'
            },
        'cabaret':
            {
            "name": __("Cabaret (20)"), 
            'description': __("Cozy and comfortable atmosphere, songs and dances, pretty hostesses, nice wine... what else do you need for the recreation? (20 sparks / decade. Get decent amusement, plus some attention and pleasure.)"),
            'cost': 20,
            'world': 'core',
            'slot': 'extra'
            },
        'whores': 
            {
            "name": __("Whores (10)"), 
            'description': __("The whores of the Ethernal Rome is the best due to the high competition at the market. (10 sparks / decade. Orgasm satisfies your eros.)"), 
            'cost': 10,
            'world': 'core',
            'slot': 'extra'
            },
        'shopping': 
            {
            "name": __("Shopping (20)"), 
            'description': __("Just sink money for meaningless purchases. (20 sparks / decade. Chaotic deed. Some random luxury make you feel prosperous.)"), 
            'cost': 20,
            'world': 'core',
            'slot': 'extra'
            },
         
    }

## RATIONS

label core_ration_cooked(person):
    #$ person.satisfy_need('nutrition', 'taste', 3)
    $ person.eat(2, 3)
    '[person.name] eats cooked food in a pub.'
    return

label core_ration_dry_half(person):
    $ person.eat(1, 0)
    $ person.tense_need('nutrition', 'hunger')
    $ person.tense_need('prosperity', 'misery')
    '[person.name] eats half ration of sublimated food'
    return

label core_ration_dry(person):
    $ person.eat(2, 0)
    $ person.tense_need('prosperity', 'misery')
    '[person.name] eats sublimated food'
    return

label core_ration_dry_double(person):
    $ person.eat(3, 0)
    $ person.tense_need('prosperity', 'misery')
    '[person.name] eats double ration of sublimated food'
    return

label core_ration_canned_half(person):
    $ person.eat(1, 0)
    $ person.tense_need('nutrition', 'hunger')
    '[person.name] eats half ration of caned food'
    return

label core_ration_canned(person):
    $ person.eat(2, 0)
    '[person.name] eats caned food'
    return

label core_ration_canned_double(person):
    $ person.eat(3, 1)
    '[person.name] eats double ration of caned food'
    return

## JOBS

label none_job_idle(person):
    '[person.name] do no job at all'
    return

label core_job_trainer(person):

    python:
        salary = person.schedule.job_productivity() * 10
        person.money += salary
        person.moral_action(orderlines='lawful')
        person.tense_need('amusement', 'gloom')
        person.satisfy_need('authority', 'supremacy', 1)
    '[person.name] trains slaves for a Guild and gains [salary] sparks'
    return


label core_job_mist_travel(person):
    python:
        worlds = [i.get_world() for i in person.get_items('navgem') if i.has_world()]
        choice = renpy.display_menu([(i.type, i) for i in worlds])
        MistTravel(core, choice, person).travel()
    return
## EXTRAS

label core_extra_promenade(person):
    "[person.name] goes to promenade. Rapture gives a minor amusement."
    $ person.satisfy_need('amusement', 'rapture', 1)
    return

label core_extra_relax(person):
    "[person.name] relaxes. Minor pleasure of comfort."
    $ person.satisfy_need('comfort', 'pleasure', 1)
    # $ person.moral_action(activity='timid')
    return

label core_extra_workout(person):
    "[person.name] does a work out. Minor activity gives adrenaline."
    $ person.satisfy_need('activity', 'adrenaline', 1)
    return

label core_extra_thuglife(person):

    python:
        result = Skillcheck(person, 'subtlety', 1).run()
        if result:
            renpy.say(None, "[person.name] mocks and abuses slaves on the square. Evil deed. Minor supremacy fuels authority needs.")
            person.satisfy_need('authority', 'supremacy', 1)
            person.moral_action(morality='evil')
        else:
            renpy.say(None, "[person.name] fails to mock anyone.")

    return

label core_extra_flirt(person):
    $ person.satisfy_need('communication', 'attention', 1)
    $ person.tense_need('eros', 'desire')
    "[person.name] flirts with strangers. Minor attention satisfies communication need. Unsatisfied desire burns eros."
    return

label core_extra_forum(person):
    $ person.satisfy_need('communication', 'attention', 2)
    python:
        result = Skillcheck(person, 'competence', 2).run()
        if result:
            renpy.say(None, "[person.name] is debating at the central forum. Minor supremacy fuels authority needs. Gets some attention.")
            person.satisfy_need('authority', 'supremacy', 1)
        else:
            person.tense_need('authority', 'humiliation')
            renpy.say(None, "[person.name] humiliated in a dispute at the forum. Gets some attention anyway.")
    return

label core_extra_perform(person):
    $ person.satisfy_need('communication', 'attention', 3)
    $ person.moral_action(activity='ardent')
    python:
        result = Skillcheck(person, 'creativity', 2).run()
        if result:
            renpy.say(None, "[person.name] performs at the central forum. Gets decent attention and minor ambition achievement.")
            person.satisfy_need('ambition', 'achievement', 1)
        else:
            person.tense_need('authority', 'humiliation')
            person.tense_need('safety', 'fear')
            renpy.say(None, "[person.name] performs at the forum. Poorly. Gets decent attention but in a humiliating and scary way.")
    return

label core_extra_library(person):
    $ person.satisfy_need('amusement', 'rapture', 2)
    $ person.satisfy_need('comfort', 'pleasure', 1)
    $ person.tense_need('activity', 'deprivation')
    "[person.name] reading books in a Grand Library of Vatican, enjoying some amusement and minor comfort. The lack of physical activity leads to deprivation."
    return

label core_extra_tippling(person):
    $ person.satisfy_need('amusement', 'rapture', 1)
    $ person.satisfy_need('communication', 'attention', 2)
    "[person.name] tippling in a bar. Some attention and minor amusement comes with cost of 10 sparks for drinks and snacks."
    return

label core_extra_cabaret(person):
    $ person.satisfy_need('amusement', 'rapture', 3)
    $ person.satisfy_need('communication', 'attention', 2)
    $ person.satisfy_need('comfort', 'pleasure', 2)
    $ person.satisfy_need('prosperity', 'opulence', 0)
    "[person.name] hanging out in an opulent cabaret. Decent amusement plus some pleasure and pleasure."
    return

label core_extra_whores(person):
    $ person.satisfy_need('eros', 'orgasm', 1)
    $ person.satisfy_need('communication', 'attention', 0)
    $ person.satisfy_need('authority', 'supremacy', 0)
    "[person.name] uses prostitutes to get a basic orgasm."
    return

label core_extra_shopping(person):
    $ person.satisfy_need('amusement', 'rapture', 1)
    $ person.satisfy_need('prosperity', 'opulence', 2)
    "[person.name] doing some meaningless purchases at the mall, feeling rich and amused."
    return


## ACCOMODATION

label core_accommodation_appartment(person):
    $ person.satisfy_need('safety', 'confidence', 2)
    $ person.satisfy_need('comfort', 'pleasure', 2)
    # '[person.name] sleeps in good appartments'
    return

label core_accommodation_unsheltered(person):
    $ person.tense_need('safety', 'fear')
    $ person.tense_need('prosperity', 'misery')
    '[person.name] sleeps on a street.'
    return

label core_accommodation_camping(person):
    '[person.name] sleeps in an improvised camp.'
    return

label core_accommodation_confined(person):
    $ person.tense_need('safety', 'fear')
    $ person.tense_need('comfort', 'pain')
    $ person.tense_need('authority', 'humiliation')
    '[person.name] is confined.'
    return

label core_accommodation_cold_floor(person):
    $ person.tense_need('prosperity', 'misery')
    '[person.name] sleeps in a crowded room.'
    return

label core_accommodation_cot_and_blanket(person):
    $ person.satisfy_need('safety', 'confidence', 0)
    $ person.satisfy_need('comfort', 'pleasure', 0)
    '[person.name] sleeps in a crowded room.'
    return

label core_accommodation_comfortable_bed(person):
    $ person.satisfy_need('safety', 'confidence', 1)
    $ person.satisfy_need('comfort', 'pleasure', 1)
    '[person.name] sleeps in a bad'
    return

label core_accommodation_private_bedroom(person):
    $ person.satisfy_need('safety', 'confidence', 2)
    $ person.satisfy_need('comfort', 'pleasure', 2)
    $ person.satisfy_need('prosperity', 'opulence', 1)
    '[person.name] sleeps in a private badroom'
    return

label core_accommodation_love_nest(person):
    return