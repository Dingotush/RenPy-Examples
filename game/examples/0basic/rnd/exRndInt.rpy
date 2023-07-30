    #
    # Dice roll examples.
    #


label exRndInt:
    $ renpy.dynamic('d6', 'df', 'dsum', 'dskill', 'dAvg', 'dHq')
    "Random integer examples"
    $ d6 = renpy.random.randint(1, 6)
    "Six sided dice: [d6]"
    $ df = renpy.random.randint(-1, 1)
    "Fudge dice: [df]"
    $ dsum = rollDice(8, 2, 3)
    "Sum 2d8+3: [dsum]"
    $ dskill = renpy.random.randrange(30, 100, 5)
    "Skill 30..95 in fives: [dskill]"
    $ dAvg = renpy.random.choice([2, 3, 3, 4, 4, 5])
    "Average dice roll: [dAvg]"
    $ dHq = renpy.random.choice(['skull', 'skull', 'skull', 'white', 'white', 'black'])
    "HeroQuest dice roll: [dHq]"

    # Ren'Py 8 / Python 3.6 or later.
    #
    if checkPyVersion(3, 6):
        "With renpy.random.choices:"
        $ dAvg = renpy.random.choices([2, 3, 4, 5], weights=[1, 2, 2, 1])[0]
        "Average dice roll: [dAvg]"
        $ dHq = renpy.random.choices(['skull', 'white', 'black'], weights=[3, 2, 1])[0]
        "HeroQuest dice roll: [dHq]"

    return