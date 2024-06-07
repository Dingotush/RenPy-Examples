init python:
    import math

    # Alternative choice screen that has an optional timeout, and can display
    # an optional count-down bar. The timeout is disabled if self-voicing is
    # being used so it then behaves like a normal menu.
    #
screen timedChoiceScr(items, seconds=0):
    default timeoutAction = None            # Action to take on a timeout
    default ticks = math.ceil(seconds * 10) # Tenths of a second, rounded up.
    default remaining = ticks               # Tenths remaining
    default timerEnabled = False
    style_prefix "choice"

    vbox:
        for item in items:
            if item.caption == ".timeout":
                $ timeoutAction = item.action
                $ timerEnabled = ticks > 0 and not _preferences.self_voicing
            elif item.caption == ".bar":
                if timerEnabled:
                    bar:
                        style "choice_bar"  # Not sure why this has to explicitly defined.
                        range ticks
                        value remaining
            else:
                textbutton item.caption:
                    action item.action
                    sensitive item.kwargs.get("sensitive", True) and item.action.get_sensitive()
    if timerEnabled:
        timer 0.1:
            repeat True
            action If(
                remaining > 0, 
                true=SetScreenVariable("remaining", remaining - 1), 
                false=timeoutAction
            )

style choice_bar is bar:
    xsize 790-200               # To match choice_button's size and padding
    xalign 0.5                  # To match choice_button's alignment

    # Timed choice example.
    #
label exTimedChoice:
    menu (screen="timedChoiceScr", seconds=3):
        "{alt}Menu. {/alt}I need to decide what to take{noalt} quickly{/noalt}!"
        ".bar":                 # Show the timeout bar as the first item.
            pass                # Never reached.
        "Take the fork":
            "You took the fork."
        "Take the spoon":
            "You took the spoon."
        ".timeout":             # Action to take on a timeout.
            "You took neither."
    return