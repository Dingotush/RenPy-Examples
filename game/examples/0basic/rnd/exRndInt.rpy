    #
    # Dice roll examples.
    #
label exRndInt:
    $ renpy.dynamic('d6', 'df', 'dsum', 'dskill', 'davg')
    "Random integer examples"
    $ d6 = renpy.random.randint(1, 6)
    "Six sided dice: [d6]"
    $ df = renpy.random.randint(-1, 1)
    "Fudge dice: [df]"
    $ dsum = rollDice(8, 2, 3)
    "Sum 2d8+3: [dsum]"
    $ dskill = renpy.random.randrange(30, 100, 5)
    "Skill 30..95 in fives: [dskill]"
    if checkPyVersion(3, 6):
        $ davg = renpy.random.choices([2, 3, 4, 5], weights=[1, 2, 2, 1])[0]
        "Average dice roll: [davg]"
    $ tmp = checkRenPyVersion(8, 1)
    return