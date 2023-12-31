#
# Messaging app contact list.
#
init 1 python:
    class AppMsgList(PhoneApp):
        def __init__(self):
            super().__init__('msgList', 'appMsgListScr', 'icon-msg-%s-40x40')
            self._contactsM = None

        # ---------------------------------------------------------------------
        # Overridden methods of PhoneApp
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def register(self, phone):
            """
            Register this application: need a reference to contacts.

            :param phone:       the phone
            """
            self._contactsM = phone._contactsM
            return

        def start(self, phone, by=None, *args):
            """
            Start this application.

            Initialise resources as needed.
            May be called while running if app didn't shut down on stop().
            Mark running as True.
            """
            super().start(phone, by, *args)
            return

        def launchMsg(self, phone, contact):
            if type(contact) is str:
                contact = phone.findContact(contact)
            if contact is None:
                return
            phone.startApp('msgDx', self, contact)

        def getStatusImg(self):
            if self.hasAnyUnseen:
                return "images/phone/icons/status-msg.png"
            return None

        def msgList(self):
            print("AppMsgList.msgList")
            result = []
            if self._contactsM:
                sortedTups = sorted(self._contactsM.items())
                for who, contact in sortedTups:
                    if contact.rx:
                        print("msgList: add '{}', {}".format(who, contact))
                        result.append((who, contact))
            return result

        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        @property
        def hasAnyUnseen(self):
            if self._contactsM is None:
                return False
            for contact in self._contactsM.values():
                if contact.unreadMsg:
                    return True
            return False

