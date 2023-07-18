

default gameOver = False        # Game over flag, set by endings
default energy = 10             # Player energy
default newDay = False          # Flag to run start of day processing
default pcLoc = 'homePer'       # Current player location

    #
    # Main game loop.
    #
label mainPer:
    # For example re-use.
    $ gameOver = False
    $ energy = 10
    $ newDay = False
    $ pcLoc = 'homePer'
    
    $ dbgLabel('mainPer')
    while not gameOver:
        if newDay:
            # Start of day processing.
            #
            call .newDay from main_new_day   # Set state for start of new day
            call .callLocLabel('wake') from main_wake    # Have the PC wake up
            $ newDay = False

        elif energy <= 0 or isLastPeriod():
            # Player character must return home to sleep now.
            #
            $ dbgLabel('main', None, 'force home/sleep energy={} lastPeriod={}', energy, isLastPeriod())
            call .travelTo('homePer') from main_day_over_travel
            call homePer.sleep from main_day_over_sleep

        else:
            # Allow the player to choose what to do.
            #
            call .callLocLabel('choice') from main_choice

    # Game over.
    #
    $ dbgLabel('mainPer', None, 'done')
    return



    # Call a local label at the player location if it exists.
    #
label .callLocLabel(localLabel):
    $ dbgLabel('mainPer', 'callLocLabel', 'localLabel="{}" pcLoc={}', localLabel, pcLoc)
    $ renpy.dynamic('renLabel')
    $ renLabel = pcLoc + '.' + localLabel
    if renpy.has_label(renLabel):
        call expression renLabel from main_call_local_label_dyn
    else:
        dbg "In main: location label [renLabel] does not exist."
    return



    # Have the player travel to a new location.
    #
label .travelTo(destLoc):
    $ dbgLabel('mainPer', 'travelTo', 'destLoc="{}" pcLoc={}', destLoc, pcLoc)
    if pcLoc == destLoc:
        return
    $ renpy.dynamic('renLabel', 'travel')
    $ travel = True
    while travel:
        $ renLabel = pcLoc + '.travelTo'
        if renpy.has_label(renLabel):
            call expression renLabel pass (destLoc) from main_travel_to_dyn
            $ travel = pcLoc != destLoc
        else:
            dbg "In travelTo: location label [renLabel] does not exist."
            # Force player location to continue.
            $ travel = False
            $ pcLoc = destLoc
    # Arrive at the location.
    call .callLocLabel('arrive') from main_travel_to_arrive
    return



    # Do housekeeping before the player wakes.
    #
label .newDay:
    $ dbgLabel('mainPer', 'newDay')
    $ energy = 10
    return