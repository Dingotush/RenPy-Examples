    #
    # Town.
    # Date/Period style.
    #
label townPer:

    # -------------------------------------------------------------------------
    # Interface labels
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Player arrives in the town from somewhere else.
    #
label .arrive:
    $ dbgLabel('townPer', 'arrive')
    if period == 0:
        "The town is quiet, nothing is open yet."
    elif period == 1 and isWorkDayPer():
        "The town is busy with people going to work."
    elif period == 4 and isWorkDayPer():
        "The town is busy with people heading home from work."
    elif period < 4:
        "There are people shopping in the town centre."
    else:
        "The town is quieter, people are going to restaurants and bars."
    $ pcLoc = 'townPer'
    return



    # Offer player a choice of what to do.
    #
label .choice:
    $ dbgLabel('townPer', 'choice')
    menu:
        "{alt}Menu. {/alt}What to do?"
        "Go to work" if isWorkDayPer():
            call .goWork from town_per_choice_work
        "Go home":
            call .goHome from town_per_choice_home
    return



    # Have the player travel to a new location.
    #
label .travelTo(destLoc):
    $ dbgLabel('townPer', 'travelTo', 'destLoc={}', destLoc)
    if destLoc == 'workPer':
        "The office you work in is a short walk from the town centre."
        $ pcLoc = destLoc
    elif destLoc == 'homePer':
        if isLastPeriod():
            "The night bus home doesn't run very frequently and you have to
            wait a while before one shows up."
        if period == 4 and isWorkDayPer():
            "The bus is packed as you and the other commuters head home."
        else:
            "The bus isn't nearly as busy it is when you commute home.
            It's almost pleasant."
        $ pcLoc = destLoc
    else:
        # Fall back if there's no specific travel message.
        "You head to your destination."
        $ pcLoc = destLoc
    return



    # -------------------------------------------------------------------------
    # Local activities
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Player character wants to go home.
    #
label .goHome:
    $ dbgLabel('townPer', 'goHome')
    call mainPer.travelTo('homePer') from town_per_go_home_travel
    return

    # Player character wants to go to work.
    #
label .goWork:
    $ dbgLabel('townPer', 'goWork')
    if period == 0:
        "It's to early to go to work, the doors won't be open."
        return
    elif period >= 4:
        "It's pointless to go to work, the office will be closed now."
        return
    call mainPer.travelTo('workPer') from town_per_go_work_travel
    return
