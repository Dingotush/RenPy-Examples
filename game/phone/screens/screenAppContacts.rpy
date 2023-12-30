#
#
#
screen appContactsScr(phone, app):
    $ phAct = phone.getMenuResponse('.phone')
    frame:
        background Frame("images/phone/wallpaper-lights.jpg")
        side "t":
            xfill True
            yfill True
            vbox:
                xfill True
                # yfill True
                text "Contacts Screen"
                text "Open [phone.isOpen]"
                text "In Menu [phone._inRpMenuM]"
                text "Items [phone.itemsStr]"
                if phAct:
                    textbutton "Thing":
                        action phAct
            