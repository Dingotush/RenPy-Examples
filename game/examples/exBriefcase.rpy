
default briefcaseLock = ComboLockFsm()

label exBriefcase:
    $ renpy.dynamic('combo', 'done', 'open', 'prompt')
    $ done = False
    $ briefcaseLock.reset()
    $ debugFsm = True
    "
    There is a briefcase here with a four digit combination lock.
    "
    while not done:
        $ open = briefcaseLock.isOpen()
        if open:
            $ prompt = "The briefcase is open."
        else:
            $ prompt = "The briefcase is closed."
        menu:
            "[prompt]"
            "Try to open it" if not open:
                if briefcaseLock.tryOpen():
                    "It pops open."
                else:
                    "Nothing happens."
            "Enter a combination":
                $ combo = renpy.input("Enter four digits", length=4, allow='0123456789')
                if len(combo) != 4:
                    "You need to set all four digits."
                else:
                    "You set the digits of the combination."
                    $ briefcaseLock.enterCombination(combo)
            "Scramble the combination":
                "You spin the numbers on the combination."
                $ briefcaseLock.enterCombination(None)
            "Close it" if open:
                "You shut the briefcase."
                $ briefcaseLock.doClose()
            "Back":
                $ done = True
                $ debugFsm = False
    return