
    # Combination lock states.
    #
define comboLockStates = (
    'locked',
    'closed',
    'open',
    'scrambled',
)


init python:

    class ComboLockFsm(Fsm):
        """
        State machine for a combination lock.
        """

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self, combination="1234"):
            """
            Construct a combination lock FSM.

            :param combination: The combination to unlock.
            """
            super(ComboLockFsm, self).__init__('comboLockStates')   # Python 2
            self._combinationM = combination


        # ---------------------------------------------------------------------
        # Inputs
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def enterCombination(self, combination):
            """
            Enter a combination.

            :param combination: The combination to try, None to scramble.
            """
            if combination is not None and combination == self._combinationM:
                # Correct.
                if self.stateName == 'locked':
                    self.stateName = 'closed'
                elif self.stateName == 'scrambled':
                    self.stateName = 'open'
            else:
                # Incorrect.
                if self.stateName == 'closed':
                    self.stateName = 'locked'
                elif self.stateName == 'open':
                    self.stateName = 'scrambled'

        def tryOpen(self):
            """
            Try to open the lock.

            :return: True if the lock is now open.
            """
            if self.stateName == 'closed':
                self.stateName = 'open'
                return True
            return False

        def doClose(self):
            """
            Close the lock.
            """
            if self.stateName == 'open':
                self.stateName = 'closed'
            elif self.stateName == 'scrambled':
                self.stateName = 'locked'

        # ---------------------------------------------------------------------
        # Outputs
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def isOpen(self):
            """
            Is the lock open?

            :return: True if it is.
            """
            return self.stateName in ('open', 'scrambled')
        