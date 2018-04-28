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
    from mer_item import Item, NavigationGem, init_default_items_data
    from mer_command import *
    from intrigue import Intrigue
    from factions import Faction
    from relations import Bond
    from motivation import Motivation
    from mer_core import *
    from mer_faction import *
    from mer_npc_actions import *
    from mer_interaction import *
    from ability import Ability
    import collections

# The game starts here.

label start:
    $ renpy.block_rollback()
    $ init_default_items_data()
    $ core = MERCore()
    $ house = core.get_house('inn')
    $ core.actions.register_actions(actions_data)
    $ Ability.make_abilities(abilities_data)
    python:
        # Init Vatican faction
        faction = CoreFaction('vatican', core_factions['vatican'])
        
        core.add_faction(faction)

        # Init npc actions
        for key, value in npc_actions_data.items():
            CoreNpcAction.add_action(key, value)
        CoreNpcAction.randomize_action(core.person_creator.gen_random_person())

        # Init interactions
        Interaction.add_interactions(interactions_data)

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
    jump lbl_game

label lbl_game:
    $ core.actions.unlock_action(player, 'gamble')
    $ core.actions.unlock_action(player, 'bazar')
    $ core.actions.unlock_action(player, 'slave_market')
    python:
        faction = core.get_faction('vatican')
        for i in range(20):
            p = core.person_creator.gen_random_person(genus='human')
            if faction.can_be_member(p):
                faction.add_member(p, 'ecclesiarchy')
                player.relations(p)
        gem = NavigationGem(WildWorld)
        player.add_item(gem)
        MistTravel(core, gem.get_world(), player, navgem=True).travel()
    call screen sc_cis(player, True)
    return

label lbl_turn_end:
    call screen sc_journal(core.get_records(), called=True)
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

