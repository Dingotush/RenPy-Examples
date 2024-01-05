#
# Base class for a phone application.
#
init python:
    class PhoneApp:

        # ---------------------------------------------------------------------
        # Construction
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        def __init__(self, name, screenName, icon=None):
            """
            Initialise an application.

            :param name:        the name of the application
            :param screenName:  the name of the screen used by this application
            :param icon:        the name of the icon image (optional)
            """
            self._nameM = name
            self._screenNameM = screenName
            self._iconM = icon
            # Initialise state.
            self._runningM = False
            self._byM = None



        # ---------------------------------------------------------------------
        # Lifecycle
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def register(self, phone):
            """
            Called when this app is added to the phone. Override for any app
            specific initialisation.

            :param phone:       the phone
            """
            return

        def start(self, phone, by=None, *args):
            """
            Start this application.

            Initialise resources as needed.
            May be called while running if app didn't shut down on stop().
            Mark running as True.
            """
            self._runningM = True
            self._byM = by
            return

        def restart(self, phone):
            """
            Restart this application.
            """
            self._runningM = True
            return

        def onOpen(self, phone, phoneOpen=False):
            """
            Called after the corresponding screen for this app has been switched
            to.

            :param phone:       the phone
            :param phoneOpen:   True if the phone screen itself just opened
            """
            print(f"{self._nameM}.onOpen")
            return

        def stop(self, phone):
            """
            Stop this application.
            Release resources.
            Mark running as False.
            """
            self._runningM = False

        def onClose(self, phone):
            """
            Called when the phone screen is dismissed.

            :param phone:       the phone
            """
            return

        def onPowerOff(self, phone):
            """
            Called when phone is being turned off.
            Release all resources and clear all state.

            :param phone:       the phone
            """
            self._runningM = False
            self._byM = None
            return

        def onConnect(self, phone):
            """
            Called when phone reconnects to the network.

            :param phone:       the phone
            """
            return

        def back(self, phone):
            """
            Go back to the previous screen.
            Default behaviour is to return to the app this was launched from, if any.
            """
            if self._byM is not None:
                phone.restartApp(self._byM)

        def backActive(self):
            """
            Should the back button be active?
            Default behaviour is to enable if this app was launched by another.

            :return:            True if it should be active
            """
            return self._byM is not None



        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        @property
        def appName(self):
            """
            Get the internal app name.
            """
            return self._nameM

        def count(self):
            return 0

        def getStatusImg(self):
            """
            Get the name of the image to display on the status line if the app
            has notifications.

            :return:            the name, or None
            """
            return None

        def hasIcon(self):
            """
            Does this app have an icon for the home screen?

            :return:            True if it does
            """
            return self._iconM is not None

        def isRunning(self):
            """
            Is this app running?

            :return:            True if it is running
            """
            return self._runningM



        # ---------------------------------------------------------------------
        # Object methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __eq__(self, other):
            """
            Compare objects for equality.

            :return:            True if they are equal
            """
            return self._nameM == other._nameM

        def __hash__(self):
            """
            Generate a hash for this object.

            :return:            the hash
            """
            return self._nameM.hash()