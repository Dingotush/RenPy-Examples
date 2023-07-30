    #
    # Date detect example.
    #
label exDateDetect:
    $ renpy.dynamic('done', 'fsm', 'prompt')
    $ fsm = DateDetectFsm()
    $ done = False
    while not done:
        $ prompt = str(fsm)
        if fsm.saySomething():
            $ prompt += "\nSay something"
        menu:
            "[prompt]"
            "Date friend":
                $ fsm.dateFriend()
            "Date other":
                $ fsm.dateOther()
            "Say something" if fsm.saySomething():
                $ fsm.saidSomething()
            "Tick":
                $ fsm.tick()
            "Back":
                $ done = True
    return