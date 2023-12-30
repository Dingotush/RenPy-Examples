#
# Trivial phone launch button.
#
screen phoneButtonScr(phone):
    frame:
        xpos 0
        xanchor 0
        ypos 0
        yanchor 0
        if phone.isOpen:
            textbutton "Phone":
                action Function(phone.close)
        else:
            textbutton "Phone":
                action Function(phone.open)