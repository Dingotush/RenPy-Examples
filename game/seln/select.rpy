    #
    # Example selection.
    #
label selection:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose Example Level"
            "Basic":
                call selnBasic from selection_basic
            "Intermediate":
                call selnInter from selection_inter
            "Advanced":
                call selnAdv from selection_adv

            "Done":
                $ done = True
    return

