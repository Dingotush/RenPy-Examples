    #
    # Intermediate example selection
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



    # Cookbook code.
    #
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
            "Timed choice":
                call exTimedChoice from seln_inter_cook_timed_choice
            "Back":
                $ done = True
    return



    # Finite state machine examples.
    #
label .fsm:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose FSM example"
            "Combination lock":
                call exBriefcase from seln_inter_fsm_briefcase
            "Date detector":
                call exDateDetect from seln_inter_fsm_date_detect
            "Back":
                $ done = True
    return



