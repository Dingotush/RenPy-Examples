    #
    # Player's home.
    # Date/Period style.
    #
label homePer:

    # -------------------------------------------------------------------------
    # Interface labels
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Player arrives home from somewhere else.
    #
label .arrive:
    $ dbgLabel('homePer', 'arrive')
    "Fishing out your key you let yourself into your home."
    $ pcLoc = 'homePer'
    return



    # Offer player a choice of what to do.
    #
label .choice:
    $ dbgLabel('homePer', 'choice')
    menu:
        "{alt}Menu. {/alt}What to do?"
        "Breakfast" if period == 0:
            call .breakfast from home_per_choice_bfast
        "Lunch" if period == 2:
            call .lunch from home_per_choice_lunch
        "Dinner" if period == 4:
            call .dinner from home_per_choice_dinner
        "Watch TV":
            call .tv from home_per_choice_tv
        "Go into town":
            call .goTown from home_per_choice_town
        "Go to work" if isWorkDayPer():
            call .goWork from home_per_choice_work
        "Sleep":
            call .sleep from home_per_choice_sleep
        "Game Over (return to cookbook examples)":
            $ gameOver = True
    return



    # Have the player travel to a new location.
    #
label .travelTo(destLoc):
    $ dbgLabel('homePer', 'travelTo', 'destLoc={}', destLoc)
    if destLoc == 'workPer':
        if period == 1:
            "The bus is packed as you and the other commuters head into town."
        else:
            "The bus isn't nearly as busy as it is in the morning.
            It's almost pleasant. Almost."
        $ pcLoc = 'townPer'
    elif destLoc == 'townPer':
        "You get the bus into town."
        $ pcLoc = destLoc
    else:
        # Fall back if there's no specific travel message.
        "You let yourself out of the house and head to your destination."
        $ pcLoc = destLoc
    return



    # Have the player wake up.
    #
label .wake:
    $ dbgLabel('homePer', 'wake')
    "You wake up rested in your own bed."
    return




    # -------------------------------------------------------------------------
    # Local activities
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Player character has breakfast.
    #
label .breakfast:
    $ dbgLabel('homePer', 'breakfast')
    "A simple bowl of cereal and a cup of life-giving coffee should
    keep you going until lunchtime."
    $ addPeriod()
    return

    # Player character makes dinner.
    #
label .dinner:
    $ dbgLabel('homePer', 'dinner')
    "A microwaved frozen meal and a beer sorts out your evening meal."
    $ addPeriod()
    return

    # Player character wants to into town.
    #
label .goTown:
    $ dbgLabel('homePer', 'goTown')
    call mainPer.travelTo('townPer') from home_go_town_travel
    return

    # Player character wants to go to work.
    #
label .goWork:
    $ dbgLabel('homePer', 'goWork')
    if period == 0:
        "It's to early to go to work, the doors won't be open."
        return

    call mainPer.travelTo('workPer') from home_go_work_travel
    return

    # Player character makes lunch.
    #
label .lunch:
    $ dbgLabel('homePer', 'lunch')
    "You fix yourself a sandwich for lunch, and have another coffee."
    $ addPeriod()
    return

    # Player wants to sleep.
    # Allow if energy is zero, and not too early.
    #
label .sleep:
    $ dbgLabel('homePer', 'sleep')
    if energy > 0 and period < 3:
        "You get into bed and toss and turn for a while,
        but it's too early to fall asleep."
        return

    "You get into bed and fall asleep."
    $ newDay = True
    if period >= 4:
        $ nextDayPer()
    else:
        $ addPeriod(2)
    return

    # Player character wants to pass time watching TV.
    #
label .tv:
    $ dbgLabel('homePer', 'tv')
    "You flop down on the couch and start channel surfing, but nothing really
    grabs you attention."
    $ addPeriod()
    return