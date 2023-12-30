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
            self._menuCaptionM = '.phone.msg.' + contact._whoM
            return

        def getMenuResponse(self, phone):
            """
            Get the action to use to start sending a message.
            
            :return:            The action, or None
            """
            return phone.getMenuResponse(self._menuCaptionM)