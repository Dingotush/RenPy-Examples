#
# Base class for a phone application.
#
init python:
    class PhoneApp:
        def __init__(self, name, screenName):
            self._nameM = name
            self._screenNameM = screenName
            # Initialise state.
            self._runningM = False

        def start(self, phone):
            """
            Start this application.

            Initialise resources as needed.
            May be called while running if app didn't shut down on stop().
            Mark running as True.
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

        def isRunning(self):
            return self._runningM

        def __eq__(self, other):
            return self._nameM == other._nameM

        def __hash__(self):
            return self._nameM.hash()