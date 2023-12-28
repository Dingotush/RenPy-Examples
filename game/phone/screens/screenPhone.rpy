#
# Phone screen
#
transform phoneShowHideTf:
    # See https://www.renpy.org/doc/html/atl.html#warpers
    on show:
        yoffset 1080
        easein_quad 1.0 yoffset 0
    on hide:
        yoffset 0
        easeout_quad 1.0 yoffset 1300

screen phoneScr(phone):
    frame at phoneShowHideTf:
        modal True              # Consume events inside frame
        xsize 0.25
        ysize 0.7
        xanchor 0.4
        yanchor 0.5
        xpos 0.3
        ypos 0.4
        xpadding 14
        ypadding 14
        background Frame("images/phone/smartphone-background.png")
        foreground Frame("images/phone/smartphone-foreground.png")
        side "c b":
            use expression phone.contentScr pass (phone)
            side "l c r":
                xfill True
                textbutton "Back":
                    sensitive phone.backActive()
                    action Function(phone.home)
                textbutton "Home":
                    xpos 0.5
                    xanchor 0.5
                    sensitive phone.homeActive()
                    action Function(phone.home)
                textbutton "Quit":
                    sensitive phone.closeActive()
                    action Function(phone.close)
        

