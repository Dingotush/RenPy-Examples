    #
    # Deck drawing examples.
    #

default drawPile = ['cat', 'dog', 'ferret', 'goldfish', 'guinea pig', 'hamster']
default discardPile = []

label exRndDeck:
    $ renpy.dynamic('done', 'pick', 'drawStr', 'dicardStr', 'peek', 'npcs', 'present')
    $ drawPile = ['cat', 'dog', 'ferret', 'goldfish', 'guinea pig', 'hamster']
    $ discardPile.clear()
    # Draw only.
    #
    "Draw only example."
    $ done = False
    while not done:
        if not drawPile:
            $ pick = None
        else:
            $ pick = renpy.random.choice(drawPile)
            $ drawPile.remove(pick)
        $ drawStr = ", ".join(drawPile)
        menu:
            "Random draw: [pick]\nDraw pile now: [drawStr]"
            "Draw again" if drawPile:
                pass
            "Next example":
                $ done = True

    # Draw and discard.
    #
    "Draw and discard example."
    $ drawPile = ['cat', 'dog', 'ferret', 'goldfish', 'guinea pig', 'hamster']
    $ discardPile.clear()
    $ done = False
    while not done:
        if not drawPile:
            $ drawPile.extend(discardPile)
            $ discardPile.clear()
        $ pick = renpy.random.choice(drawPile)
        $ drawPile.remove(pick)
        $ discardPile.append(pick)
        $ drawStr = ", ".join(drawPile)
        $ discardStr = ", ".join(discardPile)
        menu:
            "Random draw: [pick]\nDraw pile now: [drawStr]\nDiscard pile now: [discardStr]"
            "Draw again":
                pass
            "Next example":
                $ done = True

    # Shuffle and draw.
    #
    "Shuffle and draw example."
    $ drawPile = ['cat', 'dog', 'ferret', 'goldfish', 'guinea pig', 'hamster']
    $ discardPile.clear()
    $ drawStr = ", ".join(drawPile)
    "Before shuffle: [drawStr]"
    $ renpy.random.shuffle(drawPile)
    $ drawStr = ", ".join(drawPile)
    "After shuffle: [drawStr]"
    $ done = False
    while not done:
        if not drawPile:
            $ drawPile.extend(discardPile)
            $ renpy.random.shuffle(drawPile)
            $ discardPile.clear()
            $ drawStr = ", ".join(drawPile)
            "After re-shuffle: [drawStr]"
        $ pick = drawPile.pop()
        if drawPile:
            $ peek = drawPile[-1]
        else:
            $ peek = "Draw pile empty!"
        $ discardPile.append(pick)
        $ drawStr = ", ".join(drawPile)
        $ discardStr = ", ".join(discardPile)
        menu:
            "Draw: [pick]\nPeek: [peek]\nDraw pile now: [drawStr]\nDiscard pile now: [discardStr]"
            "Draw again":
                pass
            "Next example":
                $ done = True

    # Random label draw.
    #
    "Call deck of labels"
    $ drawPile = ['alleyEmpty', 'alleyCat', 'alleyVomit']
    $ discardPile.clear()
    $ done = False
    while not done:
        call callRndLabelDeck(drawPile, discardPile)
        $ drawStr = ", ".join(drawPile)
        $ discardStr = ", ".join(discardPile)
        menu:
            "Draw pile now: [drawStr]\nDiscard pile now: [discardStr]"
            "Again":
                pass
            "Next example":
                $ done = True

    # Sampling NPCs.
    #
    "Using sample to pick NPCs"
    $ npcs = ['amanda', 'brian', 'chloe', 'derek', 'emily', 'fredrick']
    $ done = False
    while not done:
        $ present = renpy.random.sample(npcs, 3)
        $ drawStr = ", ".join(present)
        menu:
            "Present: [drawStr]"
            "Again":
                pass
            "Done":
                $ done = True

    return