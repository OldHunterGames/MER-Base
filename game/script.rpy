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
    python:
        def random_relations(person):
            creator = PersonCreator()
            p1 = creator.gen_random_person()
            p2 = creator.gen_random_person()
            rel1 = person.relations(p1)
            rel2 = person.relations(p2)
            rel1.set_affection(choice([Relations.SUPPORTER, Relations.HATER, None]))
            rel1.set_distance(choice([Relations.PERSONAL, Relations.FORMAL, None]))
            rel1.set_authority(choice([Relations.DOMINANT, Relations.SUBMISSIVE, None]))
            rel2.set_affection(choice([Relations.SUPPORTER, Relations.HATER, None]))
            rel2.set_distance(choice([Relations.PERSONAL, Relations.FORMAL, None]))
            rel2.set_authority(choice([Relations.DOMINANT, Relations.SUBMISSIVE, None]))
    scene bg room
    call generate
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
    $ player = PersonCreator().gen_random_person()
    $ random_relations(player)
    call screen sc_cis(player, creation=True, controlled=True, relations=None)
    jump generate

label show_random_faction:
    python:
        leader = PersonCreator().gen_random_person()
        faction = Faction(leader)
        for i in range(14):
            faction.add_member(PersonCreator().gen_random_person())
    call screen sc_faction(faction)
    return