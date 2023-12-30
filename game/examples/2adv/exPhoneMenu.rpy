label exPhoneMenu:
    $ renpy.dynamic('apps', 'appHome', 'contacts', 'msgList', 'mom', 'phone', 'sis')
    $ appHome = AppHome()
    $ apps = []
    $ apps.append(AppContacts())
    $ apps.append(AppMsgList())
    $ apps.append(AppMsgDx())
    $ contacts = {}
    $ phone = Phone(appHome, apps, contacts)
    $ mom = phone.addContact("Mom")
    $ sis = phone.addContact("Sis")
    $ me = phone.addContactOwner("Me")
    scene bg village
    show screen phoneButtonScr(phone)
    "Tum-ti-tum"
    menu (phone, screen="phoneChoiceScr"):
        "What to do? I could use my phone."
        "Nothing":
            "You twiddle your thumbs."
        ".phone":
            "I did a phone thing."
    "Done."
    $ phone.close()
    hide screen phoneButtonScr
    pause 0.5
    scene black
    return