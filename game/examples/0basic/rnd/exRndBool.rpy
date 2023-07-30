    #
    # Coin flip tests. 
    #
label exRndBool:
    $ renpy.dynamic('heads')
    "Coin flips using util/random.rpy"
    $ heads = renpy.random.random() >= 0.5
    "Coin flip: [heads]"
    $ heads = rndProb(0.75)
    "p=0.75 chance: [heads]"
    $ heads = rndPercent(80)
    "80%% chance: [heads]"
    return