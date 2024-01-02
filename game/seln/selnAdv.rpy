    #
    # Advanced example selection.
    #
label selnAdv:
    $ renpy.dynamic("done")
    $ done = False
    while not done:
        menu:
            "Choose Advanced Example"
            "Phone":
                call exPhone from seln_adv_phone
            "Phone Menu":
                call exPhoneMenu from seln_adv_phone_menu
            "Phone Battery":
                call exPhoneBattery from seln_adv_phone_battery
            "Phone Signal":
                call exPhoneSignal from seln_adv_phone_signal
            "Back":
                $ done = True

    return
