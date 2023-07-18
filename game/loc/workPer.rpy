    #
    # Player's work.
    # Date/Period style.
    #
label workPer:

    # -------------------------------------------------------------------------
    # Interface labels
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Player arrives at work from somewhere else.
    #
label .arrive:
    $ dbgLabel('workPer', 'arrive')
    if period == 1:
        "Like ants returning to the nest you and your co-workers file in
        through the revolving doors, and scan your keycards at the barriers.
        Same old same old."
    else:
        "The revolving doors usher you into to the office building, then you
        scan your keycard at the barrier before taking the elevator up to your
        floor, and your cubicle."
    $ pcLoc = 'workPer'
    return



    # Offer player a choice of what to do.
    #
label .choice:
    $ dbgLabel('workPer', 'choice')
    menu:
        "{alt}Menu. {/alt}What to do?"
        "Lunch" if period == 2:
            call .lunch from work_per_choice_lunch
        "Work":
            call .work from work_per_choice_work
        "Go home":
            call .goHome from work_per_choice_home
    return



    # Have the player travel to a new location.
    #
label .travelTo(destLoc):
    $ dbgLabel('workPer', 'travelTo', 'destLoc={}', destLoc)
    if destLoc in ('homePer', 'townPer'):
        "You walk back into the centre of town."
        $ pcLoc = 'townPer'
    else:
        # Fall back if there's no specific travel message.
        "You leave work and head to your destination."
        $ pcLoc = destLoc
    return



    # -------------------------------------------------------------------------
    # Local activities
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Player character wants to go home.
    #
label .goHome:
    $ dbgLabel('workPer', 'goHome')
    if period == 1:
        "It really is too early to be going home. You haven't done any work yet!"
        return
    call mainPer.travelTo('homePer') from work_per_go_home_travel
    return

    # Player character wants to the town.
    #
label .goTown:
    $ dbgLabel('workPer', 'goTown')
    if period == 1:
        "It really is too early to be leaving. You haven't done any work yet!"
        return
    call mainPer.travelTo('townPer') from work_per_go_town_travel
    return


    # Player character wants to eat in the staff canteen.
    #
label .lunch:
    $ dbgLabel('workPer', 'lunch')
    "The staff canteen offers a reasonably priced lunch."
    $ addPeriod()
    return


    # Player character does some work.
    #
label .work:
    $ dbgLabel('workPer', 'work')
    if energy < 4:
        "You're too tired to work. You should probably go home."
        return
    if period >= 4:
        "Everyone else has gone home. You probably should too."
        return
    "You settle down at your desk and begin keying in data from form WS2475.
    It's dull work, but it pays the bills."
    $ pcMoney += 80
    $ energy -= 4
    $ addPeriod()
    return
