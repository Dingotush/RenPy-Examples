    #
    # Main loop example using date/period.
    #
label exMainLocPeriod:
    if config.developer:
        $ debugLabels = True    # Debug on in developer mode.

    $ pcLoc = 'homePer'         # Start at home.
    show screen datePeriodScr   # Show date/period screen.

    # Run main loop.
    #
    call mainPer from ex_main_loc_per_main

    # Final message.
    "Thank you for playing [config.name!t]."
    hide screen datePeriodScr   # Hide date/period screen.
    return
