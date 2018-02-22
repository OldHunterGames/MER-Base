image bg gt = 'bg_gt.png'
image bg river = 'bg_river.png'
image nugget = 'nugget.png'

$ world = Goldriver()

label ow_goldriver_enter(world):
    scene black

    'You leaving the Mists, entering an Outer World.'

label ow_goldriver_gt(world):
    show bg gt
    'There is a small river nearby, streaming down from the rocky hills.'

    menu:
        'Go to the river':
            call ow_goldriver_river(world)

        'Return to the Mists':
            'You leaving the Gold River Outer World'
    return

label ow_goldriver_river(world):
    show bg river
    'You moved to the river'
    "It's rocky bottom is sparking with gold."

    menu:
        'Investigate the river' if world.ingot:
            call ow_goldriver_ingot(world)

        'Extract golden send' if not world.ingot:
            call ow_goldriver_extraction(world)

        'To the Edge of Mists':
            call ow_goldriver_gt(world)

    return

label ow_goldriver_ingot(world):
    'It is indeed a gold in the river. You spot multiple golden nuggets in a bottom.'
    show nugget at top
    "In a few minutes you have a whole trade bushel of gold!"
    $ world.gold += 1
    $ world.ingot = False
    'This river still rich with a gold send, you can extract.'
    "But why bother to get more gold than you can carry off?"
    "You return to the Edge of Mists."
    hide nugget
    call ow_goldriver_gt(world)

    return

label ow_goldriver_extraction(world):
    if world.gold > 0:
        "You can extract more gold from this river, but can't carry it off. So why bother?"
    else:
        "You spend a few hours extracting gold send from the river."
        "By the end of the day you have a whole trade bushel of it. More than enough to return to Eternal Rome and sell for profit."

    "You go to the Edge of Mists."
    call ow_goldriver_gt(world)
    return
