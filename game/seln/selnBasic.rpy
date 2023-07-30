    #
    # Basic example selection
    #
label selnBasic:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose Basic Example"
            "Cookbook":
                call .cook from seln_basic_cook
            "Dialogue":
                call .dialogue from seln_basic_dialogue
            "Variables":
                call .vars from seln_basic_vars

            "Back":
                $ done = True

    return

label .cook:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose cookbook example"
            "Date/period":
                call exDatePeriod from seln_basic_cook_date_period
            "Main loop":
                call exMainLocPeriod from seln_basic_cook_main_loc_period
            "Back":
                $ done = True
    return



label .dialogue:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose dialogue example"
            "Monologue":
                call exMono from seln_basic_dia_mono
            "Narration":
                call exNarrate from seln_basic_dia_narrate
            "Back":
                $ done = True
    return



label .vars:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose variable example"
            "Floating point issues":
                call exFlt from seln_basic_vars_ex_flt
            "Money":
                call exDollarsCents from seln_basic_vars_money
            "String.format()":
                call exStrFmt from seln_basic_vars_ex_str_fmt
            "Old string interpolation":
                call exOldStrFmt from seln_basic_vars_ex_old_str_fmt
            "Back":
                $ done = True

    return