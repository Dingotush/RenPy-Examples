#
# Model of a phone or similar device.
# 
init python:
    class Phone:

        def __init__(self, homeApp, apps, contacts):
            self._homeAppM = homeApp
            self._appsM = apps
            self._contactsM = contacts
            # Init apps list.
            if not homeApp in apps:
                self._appsM.append(homeApp)
            # Init state.
            self._openM = False
            self._curAppM = None
            self.appLock = False
            self.closeLock = False

        def addContact(self, who, icon=None, history=None, rxSound=None):
            if who not in self._contactsM:
                if history is None:
                    history = []
                contact = PhoneContact(who, icon, history, rxSound)
                self._contactsM[who] = contact
            else:
                contact = findContact(who)
            return contact

        def addContactOwner(self, who, icon=None, history=None, rxSound=None):
            if who not in self._contactsM:
                if history is None:
                    history = []
                contact = PhoneContact(who, icon, history, rxSound)
                contact.rx = False
                self._contactsM[who] = contact
            else:
                contact = findContact(who)
            return contact

        def findContact(self, who):
            return self._contactsM.get(who)

        def open(self):
            # Ignore if already open.
            if self._openM:
                return
            # Select home screen if needed.
            if self._curAppM is None or not self._curAppM.isRunning():
                self.home()
            # Show and transition.
            renpy.show_screen('phoneScr', self)
            # Mark as open.
            self._openM = True

        def close(self):
            # Ignore if already closed.
            if not self._openM:
                return
            # Transition and hide
            renpy.hide_screen('phoneScr')
            # Close current app.
            if self._curAppM is not None:
                self._curAppM.stop(self)
                if not self._curAppM.isRunning():
                    self._curAppM = None
            # Mark as closed.
            self._openM = False
        
        def closeActive(self):
            return not self.appLock or self.closeLock

        def back(self):
            if self._curAppM is not None:
                self._curAppM.back(self)

        def backActive(self):
            if self._curAppM is not None:
                return self._curAppM.backActive()
            return False

        def home(self):
            """
            Start the home application.
            """
            self.startApp(self._homeAppM)

        def homeActive(self):
            return self._curAppM is not self._homeAppM

        def findApp(self, name):
            for app in apps:
                if app._nameM == name:
                    return app
            return None

        def startApp(self, app, by=None, *args):
            """
            Start an application.

            Any current app is stopped, and the new app started.

            :param app:     the new application, or its name
            :param by:      the starting application
            """
            if type(app) is str:
                app = self.findApp(app)
            if app is None:
                return
            if self._curAppM is not app:
                if self._curAppM is not None:
                    # Stop current app.
                    self._curAppM.stop(self)
                self._curAppM = app
            self._curAppM.start(self, by, *args)

        @property
        def contentScr(self):
            return self._curAppM._screenNameM



