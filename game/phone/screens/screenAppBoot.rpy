#
# Phone boot up screen.
#
screen appBootScr(phone, app):
    frame:
        background "black"
        side "t c b":
            xfill True
            yfill True
            text "myPhone":
                style 'phoneAppTitleText'
            vbox:
                xfill True
                xsize 1.0
                # xpos 0.5
                # xanchor 0.5
                # ypos 0.5
                # yanchor 0.5
                text "Booting...":
                    textalign 0.5
            bar value app.progPct range 100:
                ysize 2

        #timer app.dTimeSec action Function(phone.home)
        timer 0.1 repeat True action Function(app.tick)