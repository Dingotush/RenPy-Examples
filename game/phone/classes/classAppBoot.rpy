init 1 python:
    class AppBoot(PhoneApp):
        dTimeSec = 2.5

        def __init__(self):
            super().__init__('boot', 'appBootScr')
            self._progressM = 0
            return

        def onOpen(self, phone, phoneOpen=False):
            """
            Called after the corresponding screen for this app has been switched
            to.

            :param phone:       the phone
            :param phoneOpen:   True if the phone screen itself just opened
            """
            self._phoneM = phone
            self._progressM = 0
            return

        def onClose(self, phone):
            """
            Called when the phone screen is dismissed.

            :param phone:       the phone
            """
            self._phoneM = None
            self._progressM = 0
            return


        def tick(self):
            self._progressM += 1
            if self._progressM > self.dTimeSec * 10:
                self.onComplete()


        def onComplete(self):
            if self._phoneM is not None:
                self._phoneM.home()
            return


        @property
        def progPct(self):
            """
            Get the booting progress as a percentage 0..100.
            """
            return min(100, max(0, self._progressM * 100 / 10 / self.dTimeSec))
