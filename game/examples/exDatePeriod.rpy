    #
    # Example using date/period.
    #
label exDatePeriod:
    show screen datePeriodScr
    pc "Urrgh, Mondays. Who needs them?"

    "You stay in bed, feeling ill."
    $ addPeriod()

    "You manage to eat a little chicken soup, take an aspirin, and go back to bed."
    $ addPeriod(2)

    "You wake and check your socials, but it is all too much, and you let sleep take you again."
    $ addPeriod(5)

    "Wait ... It's lunchtime? How long did I sleep?"
    "No ... this can't be happening. Am I having a lucid dream?"
    $ addPeriod(-8)
    "Your alarm goes off, time to get ready for work."

    "End."
    hide screen datePeriodScr
    return