#
# Phone status screen.
#
screen phoneStatusScr(phone):
    style_prefix "phoneStatus"
    frame:
        background Solid("#00000040")
        xpadding 0
        top_padding 4
        bottom_padding 2
        xfill True
        side "l r":
            xfill True
            hbox:
                null width 4
                if phone.timeStr:
                    text phone.timeStr
            hbox:
                image phone.signalImg
                image phone.batteryImg
                text phone.batteryStr
                null width 4

style phoneStatus_text is default:
    size 16
