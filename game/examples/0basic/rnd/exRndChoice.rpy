    #
    # Random choice examples.
    #

    # Faces on a poker die.
    #
define pokerDiceFaces = ('9', '10', 'J', 'Q', 'K', 'A')

label exRndChoice:
    $ renpy.dynamic('face', 'faces', 'roll', 'tmp')
    "Random choice examples"
    $ face = pokerDiceFaces[renpy.random.randrange(6)]
    "Poker dice using randrange: [face]"
    $ face = renpy.random.choice(pokerDiceFaces)
    "Poker dice using choice: [face]"
    $ faces = []
    python:
        for roll in range(5):
            faces.append(renpy.random.choice(pokerDiceFaces))
        tmp = ", ".join(faces)
    "Poker dice initial roll: [tmp]"

    # Ren'Py 8 / Python 3.6 or later.
    #
    if checkPyVersion(3, 6):
        $ faces = renpy.random.choices(pokerDiceFaces, k=5)
        $ tmp = ", ".join(faces)
        "Poker dice initial roll using choices: [tmp]"

    "Random alley encounter using util/random.rpy"
    call callRndLabel(['alleyEmpty', 'alleyCat', 'alleyVomit']) from ex_rnd_choice

    # Ren'Py 8 / Python 3.6 or later.
    #
    if checkPyVersion(3, 6):
        "Random weighted alley encounter using util/random.rpy"
        call callRndLabelWeighted(['alleyEmpty', 'alleyCat', 'alleyVomit'], [2, 1, 1]) from ex_rnd_choice_weighted
    
    return
