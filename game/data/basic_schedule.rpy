init python:

    basic_jobs = {
        'idle': 
            {
                'name': __('Idle'), 
                'description': 'Idle\nJust rest and take your time for yourself.\n(Timid deed. Well rested - gain green action card.  Stagnation tenses your ambitions)', 
                'skill': None, 
                'difficulty': 0, 
                'world': None, 
                'image': 'miscards', 
            },
    }
    basic_accommodations = {
        'appartment': 
            {
            "name": __("Appartments (25)"), 
            'description': __("Standart apartments. 25 sparks/decade"), 
            'cost': 25, 
            'world': 'core'
            },
        'unsheltered':
            {
                "name": __("Unsheltered (0)"),
                "description": __(""),
                'cost': 0,
                'world': 'core'
            },
        'camping': 
            {
            "name": __("Camping"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'confined': 
            {
            "name": __("Confined"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'cold_floor': 
            {
            "name": __("Cold floor"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'cot_and_blanket': 
            {
            "name": __("Cot & Blanket"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'comfortable_bed': 
            {
            "name": __("Comfortable bed"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'private_bedroom': 
            {
            "name": __("Private bedroom"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
        'love_nest': 
            {
            "name": __("Love nest"), 
            'description': __(""), 
            'cost': 0, 
            'world': 'core'
            },
    }
    basic_rations = {
        'cooked': 
            {
            "name": __("Cooked food (20)"), 
            'description': __("Eat cooked food in a pub. 20 sparks/decade"), 
            'cost': 20, 
            'world': 'core'
            },
    }

    basic_extras = {
        'promenade': 
            {
            "name": __("Promenade (0)"), 
            'description': __("Long and thoughtful walks through the most beautiful places of the White City. (Minor entertainment. But it's free!)"), 
            'cost': 0, 
            'world': 'core'
            },
        'relax': 
            {
            "name": __("Relax (0)"), 
            'description': __("Jut take some time for a nap and make the world wait for you. (Timid deed. Get the pleasure of comfort.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'workout': 
            {
            "name": __("Workout (0)"), 
            'description': __("Workout persistently to maintain a tonus and excellent physical shape. (Get some adrenaline. It is good for your body.)"), 
            'cost': 0, 
            'world': 'core'
            },            
        'thuglife': 
            {
            "name": __("Thug life (0)"), 
            'description': __("Abuse those who are weak and mock those who can't repel you. (Ardent and evil deed. Menace or charisma check. Feeling power satisfies your authority needs.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'courtship': 
            {
            "name": __("Courtship (0)"), 
            'description': __("You can draw some romantic attends. Not necessarily serious, but enjoyable. (Timid deed. Purity or refinement check. Interaction is good to satisfy communication needs, but makes your erotic desires burn.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'flirt': 
            {
            "name": __("Flirt (0)"), 
            'description': __("Do some meaningless flirtations with a strangers. (Ardent and chaotic deed. Extravagance or charisma check. Interaction is good to satisfy communication needs, but makes your erotic desires burn.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'forum': 
            {
            "name": __("Forum (0)"), 
            'description': __("Hot philosophical and political discussions on the forum give an excellent lesson for a keen mind. (Competence or charisma check. Some interaction and minor feel of power.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'perform': 
            {
            "name": __("Perform (0)"), 
            'description': __("You will sing, dance or recite poetry. It does not matter. The main thing is to attract the awed attention of the crowd! (Ardent deed. Extravagance or refinement check. Get interaction and achievement, but public attention can be dangerous!)"), 
            'cost': 0, 
            'world': 'core'
            },
        'library': 
            {
            "name": __("Library (5)"), 
            'description': __("The Grand Library of Vatican is opened to everyone... for a fee. (5 sparks / decade. Timid and lawful deed. Enjoy some serenity and amusement, but your body will get stiff.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'tippling': 
            {
            "name": __("Tippling (5)"), 
            'description': __("Drink at the pub, chat with patrons, paw maids. (5 sparks / decade. Minor pleasure and interaction.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'gambling': 
            {
            "name": __("Gambling (10)"), 
            'description': __("Casino always wins at the end. But you can have some fun in process! (10 sparks / decade. Chaotic deed. Some pleasure and interaction.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'cabaret': 
            {
            "name": __("Cabaret (20)"), 
            'description': __("Cozy and comfortable atmosphere, songs and dances, pretty hostesses, nice wine... what else do you need for the recreation? (20 sparks / decade. Get pleasure and interaction.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'whores': 
            {
            "name": __("Whores (10)"), 
            'description': __("The whores of the Ethernal Rome is the best due to the high competition at the market. (10 sparks / decade. Orgasm satisfies your eros.)"), 
            'cost': 0, 
            'world': 'core'
            },
        'shopping': 
            {
            "name": __("Shopping (20)"), 
            'description': __("Just sink money for meaningless purchases. (20 sparks / decade. Chaotic deed. Some random luxury make you feel prosperous.)"), 
            'cost': 0, 
            'world': 'core'
            },
         
    }

## RATIONS

label core_ration_cooked(person):
    $ person.satisfy_need('nutrition', 'point', 3)
    # '[person.name] eats coocked food'
    return

## JOBS

label none_job_idle(person):
    # '[person.name] do no job at all'
    return


## EXTRAS

label core_extras_promenade(person):
    return

label core_extras_relax(person):
    return

label core_extras_workout(person):
    return

label core_extras_thuglife(person):
    return

label core_extras_courtship(person):
    return

label core_extras_flirt(person):
    return

label core_extras_forum(person):
    return

label core_extras_perform(person):
    return

label core_extras_library(person):
    return

label core_extras_tippling(person):
    return

label core_extras_gambling(person):
    return

label core_extras_cabaret(person):
    return

label core_extras_whores(person):
    return

label core_extras_shopping(person):
    return


## ACCOMODATION

label core_accommodation_appartment(person):
    $ person.satisfy_need('comfort', 'point', 3)
    # '[person.name] sleeps in good appartments'
    return

label core_accommodation_unsheltered(person):
    return

label core_accommodation_camping(person):
    return

label core_accommodation_confined(person):
    return

label core_accommodation_cold_floor(person):
    return

label core_accommodation_cot_and_blanket(person):
    return

label core_accommodation_comfortable_bed(person):
    return

label core_accommodation_private_bedroom(person):
    return

label core_accommodation_love_nest(person):
    return