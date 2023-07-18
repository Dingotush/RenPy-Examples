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

            "Done":
                $ done = True
    return

