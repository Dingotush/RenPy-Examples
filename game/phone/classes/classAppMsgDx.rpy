#
# Messaging app send/receive.
#
init 1 python:
    class AppMsgDx(PhoneApp):
        def __init__(self):
            super().__init__('msgDx', 'appMsgDxScr')

        def start(self, phone, by=None, contact=None, *args):
            """
            Start this application.

            Initialise resources as needed.
            May be called while running if app didn't shut down on stop().
            Mark running as True.
            """
            super().start(phone, by, *args)
            self._contactM = contact
            self._runningM = True
            self._byM = by
            return