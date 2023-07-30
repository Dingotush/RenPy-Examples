
    # Date detection states.
    #
define dateDetectStates = (
    'notSeen',          # 0
    'dateFirst',        # 1
    'dateSecond',       # 2
    'worried',          # 3
    'saySomething',     # 4
)



init python:

    class DateDetectFsm(FsmTimer):
        """
        State machine for detecting dates.
        """

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self):
            """
            Construct a date detecting FSM.
            """
            super(DateDetectFsm, self).__init__('dateDetectStates')   # Python 2
            # super().__init__('dateDetectStates')                    # Python 3


        # ---------------------------------------------------------------------
        # Timer methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def timerTriggered(self):
            """
            Back off detection state after timer has elapsed.
            Called when timer reaches zero.
            """
            if self.stateName == 'dateFirst':
                self.stateName = 'notSeen'
                del self.timerTrig
            elif self.stateName == 'dateSecond':
                self.stateName = 'dateFirst'
                self.timer = 7
                del self.timerTrig
            elif self.stateName == 'worried':
                self.stateName = 'dateSecond'
                self.timer = 7
                del self.timerTrig



        # ---------------------------------------------------------------------
        # Inputs
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def dateFriend(self):
            """
            PC seen on date with friend.
            """
            if self.stateName == 'notSeen':
                self.stateName = 'dateFirst'
                self.timer = 7
            elif self.stateName == 'dateFirst':
                self.stateName = 'dateSecond'
                self.timer = 7
            elif self.stateName == 'worried':
                self.stateName = 'saySomething'
                self.timer = 7

        def dateOther(self):
            """
            PC seen on a date with someone else.
            """
            if self.stateName == 'dateSecond':
                self.stateName = 'worried'
                self.timer = 7

        def saidSomething(self):
            """
            Said something to the PC.
            """
            if self.stateName == 'saySomething':
                self.stateName = 'dateSecond'
                self.timer = 7

        # ---------------------------------------------------------------------
        # Outputs
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def saySomething(self):
            """
            NPC ready to confront PC.
            """
            return self.stateName == 'saySomething'
