#
# A phone contact.
#
init python:
    class PhoneContact:

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self, phone, who, icon, msgHist):
            self._phoneM = phone
            self._whoM = who
            self.icon = icon
            # Message lists
            self._msgHistM = msgHist    # History
            self._msgUnseenM = []       # Unseen
            self._msgQueueM = []        # Queued (not on phone)
            # Direction.
            self.rx = True

        # ---------------------------------------------------------------------
        # Network
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def onConnect(self, phone):
            """
            Called when phone reconnects to the network.
            Transfer queued items to unseen.

            :param phone:       the phone
            """
            if self._msgQueueM:
                self._msgUnseenM.extend(self._msgQueueM)
                self._msgQueueM.clear()
                self._phoneM.playMsgRxSound()
            return

        # ---------------------------------------------------------------------
        # Messages
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def msgQueue(self, post):
            self._msgQueueM.append(post)

        def msgUnseen(self, post):
            self._msgUnseenM.append(post)
            if post.rx:
                self._phoneM.playMsgRxSound()
            else:
                self._phoneM.playMsgTxSound()

        def msgSeeAll(self):
            self._msgHistM.extend(self._msgUnseenM)
            self._msgUnseenM.clear()

        def sms(self, what):
            post = PhoneMsg(True, what)
            self.msgUnseen(post)

        def smsReply(self, what):
            post = PhoneMsg(False, what)
            self.msgUnseen(post)

        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        @property
        def unreadMsg(self):
            return len(self._msgUnseenM)

