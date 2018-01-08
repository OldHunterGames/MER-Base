# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init -10 python:
    sys.path.append(renpy.loader.transfn("scripts"))
    sys.path.append(renpy.loader.transfn("scripts/person"))
    sys.path.append(renpy.loader.transfn("core"))
    from mer_person import *
    from mer_utilities import *
    from mer_item import Item, init_default_items_data
    from mer_command import *
    from intrigue import Intrigue
    from factions import Faction
    from relations import Bond
    from motivation import Motivation
    from mer_core import *
    import collections

# The game starts here.

label start:
    $ renpy.block_rollback()
    $ init_default_items_data()
    $ core = MERCore()
    $ house = core.get_house('inn')
    $ core.actions.register_actions(actions_data)
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room
    jump  generate
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label generate:
    $ core.create_player()
    call screen sc_gen_player()
    $ player = core.player
    $ core.unlock_schedule(player)
    $ core.actions.unlock_action(player, 'gamble')
    # call screen sc_gen_faction()
    jump lbl_game

label lbl_make_faction:
    python:
        leader = PersonCreator().gen_random_person()
        faction = Faction(leader)
        core.faction = faction
    return

label lbl_game:
    # $ make_intrigues(core.faction, core.player)
    call lbl_make_faction
    call screen sc_cis(player, True)
    call lbl_contacts(player)
    return

label lbl_turn_end:
    call screen sc_journal(core.get_records(), called=True)
    return

label lbl_wish_test():
    # for wish system testing
    python:
        person = core.person_creator.gen_random_person()
        core.faction.add_member(person)
        for i in range(0, 10):
            new = core.person_creator.gen_random_person()
            if i == 5:
                person.add_bond(Bond(new, 'friend'))
            if i == 7:
                person.add_bond(Bond(new, 'ally'))
            new.add_bond(Bond(person, 'friend'))
        for i in range(0, 10):
            new = core.person_creator.gen_random_person()
            if i == 5:
                person.add_bond(Bond(new, 'rival'))
            if i == 7:
                person.add_bond(Bond(new, 'traitor'))
            if i == 9:
                person.add_bond(Bond(new, 'offender'))
            new.add_bond(Bond(person, 'rival'))

        player.relations(person)
        for key in wishes_data.keys():
            core.wish_maker.reserve_wish(person, key)
            core.wish_maker.process_wishes(person)
    return

label lbl_jobcheck(schedule_obj, person):
    '[person.name] works with productivity: [schedule_obj.productivity]'
    python:
        attribute = schedule_obj.attribute
        if getattr(person, attribute)() > schedule_obj.productivity:
            schedule_obj.productivity += 1
            productivity_info = 'Productivity raised'
        else:
            productivity_info = 'Productivity is max for %s' % person.name
    '[productivity_info]'
    return