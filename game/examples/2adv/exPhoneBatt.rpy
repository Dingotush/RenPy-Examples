label exPhoneBattery:
    $ renpy.dynamic('apps', 'appHome', 'contacts', 'msgList', 'mom', 'phone', 'sis')
    $ appHome = AppHome()
    $ phone = Phone()
    $ me = phone.addContactOwner("Me")
    $ mom = phone.addContact("Mom")
    $ sis = phone.addContact("Sis")
    scene bg village
    $ phone.battery = 0
    $ phone.open()
    $ phone.closeLock=True
    "I better put my phone on to charge."
    $ phone.charging = True
    $ phone.battery = 33
    "This phone charges really quickly."
    $ phone.battery = 66
    "I can disconnect it now."
    $ phone.battery = 100
    $ phone.charging = False
    "It drains fast too."
    $ phone.battery = 99
    "Look at that."
    $ phone.battery = 80
    "I ought to get that looked at."
    $ phone.battery = 60
    "It might need a new battery."
    $ phone.battery = 40
    "I hope the battery doesn't swell up and become a danger pillow."
    $ phone.battery = 20
    "Or maybe a new phone."
    $ phone.battery = 1
    "I don't think it's long for this world."
    $ phone.battery = 0
    "And it's gone!"
    "Done."
    $ phone.closeLock=False
    $ phone.close()
    hide screen phoneButtonScr
    pause 0.5
    scene black
    return