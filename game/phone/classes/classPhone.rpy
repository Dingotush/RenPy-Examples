#
# Model of a phone or similar device.
#

default phoneList = []          # List of phones needing callbacks

init python:

    def phoneModeCallback(newMode, oldModes):
        """
        Called when Ren'Py changes modes. Used to notify phones of transition
        into and out of menus.

        See https://www.renpy.org/doc/html/modes.html#default-modes

        :param newMode:         The new mode
        :param oldModes:        A list of old modes
        """
        # Ignore trivial cases.
        if not oldModes or newMode == oldModes[0]:
            return
        # Entering a menu is interesting.
        #
        if newMode == 'menu':
            for phone in phoneList:
                phone.changeMenuMode(True)
        # These modes are not interesting.
        #
        elif newMode in ('start', 'say', 'screen', 'imagemap', 'input'):
            for phone in phoneList:
                phone.changeMenuMode(False)

    # Register callback.
    #
    config.mode_callbacks.append(phoneModeCallback)

    class Phone:
        """
        Representation of a smart phone.
        """

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self, homeApp, apps, contacts):
            self._homeAppM = homeApp
            self._appsM = apps
            self._contactsM = contacts
            # Init apps list.
            if not homeApp in apps:
                self._appsM.append(homeApp)
            for app in self._appsM:
                app.register(self)
            # Owner.
            self._ownerM = None         # Owner's own contact details.
            # Msg system.
            self.msgRxSound = "audio/phone/msg-rx.ogg"
            self.msgTxSound = "audio/phone/msg-tx.ogg"
            # Init state.
            self._openM = False         # Phone screen is open
            self._curAppM = None        # Current application object
            self.appLock = False        # Application locked, player can't use back/home/close
            self.closeLock = False      # Close locked, player can't use close button
            self._batteryM = 100        # Battery level
            self._chargingM = False     # On charge
            self._powerOnM = False      # Powered on
            self._signalM = 100         # Signal strength
            self.timeStr = "00:00"      # Time of day for status line
            # Menu interactions.
            self._inRpMenuM = False     # Choice menu active
            self._menuScannedM = False  # Choice menu entries were scanned
            self._phoneItemsM = []      # Collected phone caption, action pairs
            # Register phone for filtered Ren'Py mode callbacks.
            phoneList.append(self)



        # ---------------------------------------------------------------------
        # Contacts
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def addContact(self, who, icon=None, history=None):
            """
            Add a new contact.

            :param who:         The contact's name
            :param icon:        The contact's icon, default None
            :param msgHist:     The message history, default None
            :return:            The contact
            """
            if who not in self._contactsM:
                if history is None:
                    history = []
                contact = PhoneContact(self, who, icon, history)
                self._contactsM[who] = contact
            else:
                contact = findContact(who)
            return contact

        def addContactOwner(self, who, icon=None, history=None):
            """
            Add a contact for the phone's owner.

            :param who:         The contact's name
            :param icon:        The contact's icon, default None
            :param msgHist:     The message history, default None
            :return:            The contact
            """
            if who not in self._contactsM:
                if history is None:
                    history = []
                contact = PhoneContact(self, who, icon, history)
                contact.rx = False
                self._ownerM = contact
                self._contactsM[who] = contact
            else:
                contact = findContact(who)
            return contact

        def findContact(self, who):
            """
            Find a contact.

            :param who:         The contact's name
            :return:            The contact, or None
            """
            return self._contactsM.get(who)


        # ---------------------------------------------------------------------
        # Controls
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def open(self):
            # Ignore if already open.
            if self._openM:
                return
            # Booting?
            boot = self.hasPower and not self._powerOnM
            if boot:
                # Show boot screen it available.
                self._curAppM = None
                self.startApp('boot')
                # Otherwise straight to home screen.
                if not self._curAppM:
                    self.home()
                # Connect to network.
                self.connect()
            elif self._curAppM is None or not self._curAppM.isRunning():
                self.home()
            # Show and transition.
            renpy.show_screen('phoneScr', self)
            # Mark as open.
            self._openM = True
            if self.hasPower:
                renpy.restart_interaction()
                self._curAppM.onOpen(self, True)

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
            return not self.appLock and not self.closeLock

        def back(self):
            if self._curAppM is not None:
                self._curAppM.back(self)

        def backActive(self):
            if not self.appLock and self._curAppM is not None:
                return self._curAppM.backActive()
            return False

        def home(self):
            """
            Start the home application.
            """
            self.startApp(self._homeAppM)

        def homeActive(self):
            return not self.appLock and self._curAppM is not self._homeAppM

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
            if self._openM and self.hasPower:
                renpy.restart_interaction()
                self._curAppM.onOpen(self)

        def restartApp(self, app):
            """
            Restart an application.

            Any current app is stopped, and the new app started.

            :param app:     the new application, or its name
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
            self._curAppM.restart(self)
            if self._openM and self.hasPower:
                renpy.restart_interaction()
                self._curAppM.onOpen(self)

        def powerOff(self):
            """
            Power off the phone.
            """
            self._powerOnM = False
            if self._curAppM is not None:
                # Stop current app.
                self._curAppM.stop(self)
            self._curAppM = None
            for app in self._appsM:
                app.onPowerOff(self)

        def connect(self):
            """
            Phone reconnecting to the network.
            """
            for contact in self._contactsM.values():
                contact.onConnect(self)
            for app in self._appsM:
                app.onConnect(self)

        # ---------------------------------------------------------------------
        # Message system characters
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def msgCharRx(self, contact):
            """
            Get a character that the phone owner can receive messages from.

            :param contact:     Either a contact or the who name of a contact
            :return:            A character that can be used to "say" things
            """
            if type(contact) is str:
                contact = self.findContact(contact)
            return PhoneMsgCharacter(phone, contact, True)

        def msgCharTx(self, contact):
            """
            Get a character that the phone owner can send messages to.

            :param contact:     Either a contact or the who name of a contact
            :return:            A character that can be used to "say" things
            """
            if type(contact) is str:
                contact = self.findContact(contact)
            return PhoneMsgCharacter(phone, contact, False)

        def playMsgRxSound(self):
            if self.msgRxSound:
                renpy.sound.play(self.msgRxSound)

        def playMsgTxSound(self):
            if self.msgTxSound:
                renpy.sound.play(self.msgTxSound)

        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        @property
        def app(self):
            """
            The current application instance.

            :return:            the currect application, or None
            """
            return self._curAppM

        @property
        def battery(self):
            """
            Get the battery level as a percentage 0..100.

            :return:            the battery level
            """
            return self._batteryM

        @battery.setter
        def battery(self, value):
            """
            Set the battery level as  percentage 0..100.

            :param value:       the new level
            """
            self._batteryM = max(0, min(100, int(round(value))))
            if not self.hasPower:
                self.powerOff()

        @property
        def batteryImg(self):
            if self._chargingM:
                result = "chg"
            elif self._batteryM == 0:
                result = "0"
            else:
                result = str((self._batteryM + 19) // 20)
            return "images/phone/icons/battery-{}.png".format(result)

        @property
        def batteryStr(self):
            return "{}%".format(self._batteryM)

        @property
        def charging(self):
            return self._chargingM

        @charging.setter
        def charging(self, value):
            self._chargingM = value
            if not self.hasPower:
                self.powerOff()

        @property
        def contentScr(self):
            """
            Get the current screen name.

            :return:            the current application screen name
            """
            return self._curAppM._screenNameM

        @property
        def hasPower(self):
            return self._chargingM or self._batteryM

        @property
        def hasSignal(self):
            """
            Does the phone have a connection to the network?

            :return:            True if it does
            """
            return self._signalM and self.hasPower

        @property
        def isOpen(self):
            return self._openM

        @property
        def itemsStr(self):
            if self._phoneItemsM:
                return ", ".join([item.caption for item in self._phoneItemsM])
            return "None"

        @property
        def rdyChoice(self):
            """
            Is the phone ready to accept choice menu items?

            :return:            True if phone is ready to scan menu items
            """
            return not self._menuScannedM

        @property
        def signal(self):
            return self._signalM

        @property
        def signalImg(self):
            if self._signalM == 0:
                result = "0"
            else:
                result = str((self._signalM + 19) // 20)
            return "images/phone/icons/signal-{}.png".format(result)

        @signal.setter
        def signal(self, value):
            """
            Set the signal level as  percentage 0..100.

            :param value:       the new level
            """
            connected = self.hasSignal
            self._signalM = max(0, min(100, int(round(value))))
            if not connected and self.hasSignal:
                self.connect()

        @property
        def statusImgs(self):
            result = []
            for app in self._appsM:
                img = app.getStatusImg()
                if img is not None:
                    result.append(img)
            return result



        # ---------------------------------------------------------------------
        # Choice menu interaction and callback
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def changeMenuMode(self, menuMode=False):
            """
            Called when Ren'Py's mode changes to and from "menu".

            :param menuMode:    True if i a choice menu
            """
            if not menuMode:
                self._menuScannedM = False
            self._inRpMenuM = menuMode

        def scanMenuCaptions(self, items):
            """
            Scan a choice menu list for captions the phone can respond to.

            :param items:       The choice menu items
            """
            if self._menuScannedM:
                return
            self._phoneItemsM.clear()
            for item in items:
                if item.action is not None and item.caption.startswith('.phone'):
                    self._phoneItemsM.append(item)
            self._menuScannedM = True

        def getMenuResponse(self, caption):
            """
            Get any action caught for a given phone caption.

            Actions are usually of type ChoiceAction.

            :param caption:     The caption. Eg. ".phone.abc.xyz"
            :return:            The action or None
            """
            if not self._inRpMenuM:
                return None
            for item in self._phoneItemsM:
                if item.caption == caption:
                    return item.action
            return None
                




