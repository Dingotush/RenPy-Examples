#
# Messaging app contact list.
#
init 1 python:
    class AppMsgList(PhoneApp):
        def __init__(self):
            super().__init__('msgList', 'appMsgListScr', 'icon-msg-%s-40x40')

        def start(self, phone, by=None, *args):
            """
            Start this application.

            Initialise resources as needed.
            May be called while running if app didn't shut down on stop().
            Mark running as True.
            """
            super().start(phone, by, *args)
            self._contactsM = phone._contactsM
            return

        def launchMsg(self, phone, contact):
            if type(contact) is str:
                contact = phone.findContact(contact)
            if contact is None:
                return
            phone.startApp('msgDx', self, contact)


        def msgList(self):
            result = []
            sortedTups = sorted(self._contactsM.items())
            for who, contact in sortedTups:
                if contact.rx:
                    result.append((who, contact))
            return result