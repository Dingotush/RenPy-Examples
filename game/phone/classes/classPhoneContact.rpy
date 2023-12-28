#
# A phone contact.
#
init python:
    class PhoneContact:
        def __init__(self, who, icon, history, rxSound=None):
            self._whoM = who
            self.icon = icon
            self._historyM = history
            self.rxSound = rxSound
            self._unreadM = 0
            self.rx = True


        def sms(self, what):
            post = (True, what)
            self._historyM.append(post)
            self._unreadM += 1

        def smsReply(self, what):
            post = (False, what)
            self._historyM.append(post)
            self._unreadM += 1

        @property
        def unreadMsg(self):
            return self._unreadM

        @unreadMsg.deleter
        def unreadMsg(self):
            self._unreadM = 0
