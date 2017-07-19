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
    from mer_core import *
    import collections

# The game starts here.

label start:
    $ renpy.block_rollback()
    $ init_default_items_data()
    $ core = MERCore()
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
    # call screen sc_gen_faction()
    call lbl_make_faction
    jump lbl_game

label lbl_make_faction:
    python:
        leader = PersonCreator().gen_random_person()
        faction = Faction(leader)
        for i in range(14):
            faction.add_member(PersonCreator().gen_random_person())
        core.faction = faction
    return

label lbl_game:
    call screen sc_cis(player, controlled=True)
    return

label lbl_turn_end:
    python:
        make_intrigues(core.faction)