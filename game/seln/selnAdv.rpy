    #
    # Advanced example selection.
    #
label selnAdv:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose Advanced Example"
            "Phone":
                call exPhone from seln_adv_fsm
            "Back":
                $ done = True

    return
