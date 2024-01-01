label exPhoneMenu:
    $ renpy.dynamic('apps', 'appHome', 'contacts', 'msgList', 'mom', 'phone', 'sis')
    $ appHome = AppHome()
    $ apps = []
    $ apps.append(AppContacts())
    $ apps.append(AppMsgList())
    $ apps.append(AppMsgDx())
    $ contacts = {}
    $ phone = Phone(appHome, apps, contacts)
    $ me = phone.addContactOwner("Me")
    $ mom = phone.addContact("Mom")
    $ sis = phone.addContact("Sis")
    scene bg village
    show screen phoneButtonScr(phone)
    "Tum-ti-tum"
    menu (phone, screen="phoneChoiceScr"):
        "What to do? I could text my sister."
        "No, she's probably busy.":
            call .mom
        ".phone":
            "I did a phone thing."
        ".phone.msg.Sis":
            call .sis
    "Done."
    $ phone.close()
    hide screen phoneButtonScr
    pause 0.5
    scene black
    return

label .sis:
    $ renpy.dynamic('pc', 'sis')
    $ phone.changeMenuMode()
    $ pc = phone.msgCharTx("Sis")
    $ sis = phone.msgCharRx("Sis")
    pause 0.1
    pc "Hi sis. What's up?"
    sis "Nothing. You?"
    return

label .mom:
    $ renpy.dynamic('pc', 'mom')
    $ pc = phone.msgCharTx("Mom")
    $ mom = phone.msgCharRx("Mom")
    "I guess I should start cleaning the kitchen. Joy."
    $ mom.openMsgSystem()
    mom "Do you still have my casserole dish?"
    pc "I was just about to clean it when you messaged me."
    mom "Oh, that's good."
    $ mom.closeMsgSystem()
    "
    You start to run the hot water into the sink.
    "
    $ mom.openMsgSystem()
    mom "Only I'll need it for the dinner party tonight."
    pc "Fine, I'll bring it over as soon as it's clean."
    $ mom.closeMsgSystem()
    return

