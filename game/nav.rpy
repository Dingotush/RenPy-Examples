#
# Navigation.
# E&OE.
#
    # Allow PC to choose a new location.
    #
label navigate:
    # Default to staying put.
    #
    $ newLoc = pcLoc

    # If self voicing use spoken navigation menu,
    # otherwise use navigation screen.
    # Both just change newLoc.
    #
    if _preferences.self_voicing:
        call .navMenu
    else:
        call screen navScr

    # Did they pick somewhere new?
    #
    if newLoc != pcLoc:
        # Describe how they get from pcLoc to newLoc.
        # ...
        # Put the PC at the new location.
        $ pcLoc = newLoc
    return



    # Present a list of places to go.
    #
label .navMenu:
    menu:
        "{alt}Menu. {/alt}Where should I go?"
        "Beach" if pcLoc != 'beach':
            $ newLoc = 'beach'
        "Gym" if pcLoc != 'gym':
            $ newLoc = 'gym'
        "Home" if pcLoc != 'home':
            $ newLoc = 'home'
        "Pub" if pcLoc != 'pub':
            $ newLoc = 'pub'
        "Stay here":
            pass
    return



    # Ugly AF navigation screen.
    # Replace with pretty map with markers and mouseover hot spots and put
    # in its own rpy file.
    #
screen navScr():
    vbox:
        button:
            text "Beach"
            action SetVariable('newLoc', 'beach')
        button:
            text "Gym"
            action SetVariable('newLoc', 'gym')
        button:
            text "Home"
            action SetVariable('newLoc', 'home')
        button:
            text "Pub"
            action SetVariable('newLoc', 'pub')
            