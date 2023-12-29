
label exPhone:
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
    "Open"
    $ phone.open()
    "Rx text"
    $ msgApp = phone.findApp('msgList')
    $ phone.startApp(msgApp)
    $ msgApp.launchMsg(phone, mom)
    #$ phone.startApp('msgDx', None, mom)
    $ phone.appLock = True
    $ sis.sms("Can I ask you something?")
    $ mom.sms("Hi")
    "Msgs"
    $ mom.sms("Hello?")
    $ mom.sms("Anyone home?")
    $ mom.sms("Are you {i}alive{/i}?")
    "More"
    $ mom.sms("I'm getting really worried now.")
    "More"
    $ mom.sms("Seriously, call me. If you don't I'm coming straight over.")
    menu:
        "How do you reply?"
        "Just getting up":
            $ mom.smsReply("I'm fine, just waking up.")
        "In the shower":
            $ mom.smsReply("I'm fine, just got out of the shower.")
    "More"
    $ mom.sms("Your sister has been trying to get in touch with you.")
    $ phone.appLock = False
    "Close"
    $ phone.close()
    "Done"
    hide bg
    return