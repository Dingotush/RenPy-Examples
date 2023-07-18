    #
    # Basic example selection
    #
label selnInter:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose Intermediate Example"
            "Finite state machines":
                call .fsm from seln_inter_fsm
            "Cookbook":
                call .cook from seln_inter_cook
            "Back":
                $ done = True

    return

label .cook:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose cookbook example"
            "Base FSM":
                call exFsm from seln_inter_cook_fsm
            "Base FSM Timer":
                call exFsmTimer from seln_inter_cook_fsm_timer
            "Back":
                $ done = True
    return

label .fsm:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose FSM example"
            "Combination lock":
                call exBriefcase from seln_inter_fsm_briefcase
            "Back":
                $ done = True
    return



