#
# Phone screen
#

# Transforms.
#
# See https://www.renpy.org/doc/html/atl.html#warpers
#
transform phoneShowTf:
    on show:
        yoffset 1080
        easein_quad 1.0 yoffset 0

transform phoneHideTf:
    yoffset 0
    easeout_quad 1.0 yoffset 1300

transform phoneShowHideTf:
    on show:
        yoffset 1080
        easein_quad 1.0 yoffset 0
    on hide:
        yoffset 0
        easeout_quad 1.0 yoffset 1300

screen phoneScr(phone):
    frame at phoneShowHideTf:
        modal True              # Consume events inside frame
        xsize phone.xsize
        ysize phone.ysize
        xanchor 0.4
        yanchor 0.5
        xpos 0.3
        ypos 0.4
        xpadding 14
        ypadding 14
        background Frame("images/phone/smartphone-background.png")
        foreground Frame("images/phone/smartphone-foreground.png")
        if phone.hasPower:
            side "c b":
                use expression phone.contentScr pass (phone, phone.app)
                side "l c r":
                    xfill True

                    imagebutton:
                        auto "images/phone/icons/but-back-%s.png"
                        xpos 0.5
                        xanchor 0.5
                        ypos 0.5
                        yanchor 0.5
                        xpadding 20
                        top_padding 4
                        sensitive phone.backActive()
                        action Function(phone.back)
                    imagebutton:
                        auto "images/phone/icons/but-home-%s.png"
                        xpos 0.5
                        xanchor 0.5
                        ypos 0.5
                        yanchor 0.5
                        top_padding 4
                        sensitive phone.homeActive()
                        action Function(phone.home)
                    imagebutton:
                        auto "images/phone/icons/but-quit-%s.png"
                        xpos 0.5
                        xanchor 0.5
                        ypos 0.5
                        yanchor 0.5
                        xpadding 20
                        top_padding 4
                        sensitive phone.closeActive()
                        action Function(phone.close)
#                    textbutton "Back":
#                        sensitive phone.backActive()
#                        action Function(phone.back)
#                    textbutton "Home":
#                        xpos 0.5
#                        xanchor 0.5
#                        sensitive phone.homeActive()
#                        action Function(phone.home)
#                    textbutton "Quit":
#                        sensitive phone.closeActive()
#                        action Function(phone.close)
        

