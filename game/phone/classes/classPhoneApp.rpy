#
# Base class for a phone application.
#
init python:
    class PhoneApp:
        def __init__(self, name, screenName, icon=None):
            self._nameM = name
            self._screenNameM = screenName
            self._iconM = icon
            # Initialise state.
            self._runningM = False
            self._byM = None

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

        def stop(self, phone):
            """
            Stop this application.
            Release resources.
            Mark running as False.
            """
            self._runningM = False
            return

        def back(self, phone):
            if self._byM is not None:
                phone.restartApp(self._byM)

        def backActive(self):
            return self._byM is not None

        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def count(self):
            return 0

        def hasIcon(self):
            return self._iconM is not None

        def isRunning(self):
            return self._runningM


        # ---------------------------------------------------------------------
        # Object methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __eq__(self, other):
            return self._nameM == other._nameM

        def __hash__(self):
            return self._nameM.hash()