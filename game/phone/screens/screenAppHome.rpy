#
# Home screen
#
screen appHomeScr(phone):
    frame:
        background Frame("images/phone/wallpaper-lights.jpg")
        vbox:
            xfill True
            yfill True
            text "Home Screen"
            textbutton "Contacts":
                action Function(phone.startApp, 'contacts')