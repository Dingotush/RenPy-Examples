#
# A phone contact.
#
init python:
    class PhoneContact:
        def __init__(self, who, icon, msgHist, rxSound=None):
            self._whoM = who
            self.icon = icon
            self._msgHistM = msgHist
            self.rxSound = rxSound
            self._unreadM = 0
            self.rx = True


        def sms(self, what):
            post = (True, what)
            self._msgHistM.append(post)
            self._unreadM += 1

        def smsReply(self, what):
            post = (False, what)
            self._msgHistM.append(post)
            self._unreadM += 1

        @property
        def unreadMsg(self):
            return self._unreadM

        @unreadMsg.deleter
        def unreadMsg(self):
            self._unreadM = 0
