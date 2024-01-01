#
# Home screen
#
screen appHomeScr(phone, app):
    frame:
        background Frame("images/phone/wallpaper-lights.jpg")
        xpadding 0
        ypadding 0
        side "t c":
            xfill True
            yfill True
            use phoneStatusScr(phone)
            vbox:
                xfill True
                yfill True
                text "Home Screen"
                vpgrid:
                    cols 4
                    spacing 5
                    draggable True
                    mousewheel True
                    # scrollbars "vertical"

                    for app in phone._appsM:
                        if app.hasIcon():
                            imagebutton:
                                auto app._iconM
                                action Function(phone.startApp, app)
                    textbutton "Contacts":
                        action Function(phone.startApp, 'contacts')