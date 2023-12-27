#
# Phone screen
#
screen phoneScr(phone):
    frame:
        modal True              # Consume events inside frame
        xsize 0.3
        ysize 0.7
        xanchor 0.4
        yanchor 0.5
        xpos 0.5
        ypos 0.4
        xpadding 10
        ypadding 10
        background Frame("images/phone/phone_background.png")
        vbox:
            text "Phone"
