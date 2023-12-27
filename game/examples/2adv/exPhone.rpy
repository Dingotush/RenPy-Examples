default appHome = AppHome()
default apps = []
default phone = Phone(appHome, apps)

label exPhone:
    "Open"
    $ phone.open()
    "Close"
    $ phone.close()
    "Done"
    return