#
# Finite State Machine with ticks and timer.
#
# Note: This is for Python 2.7/RenPy 7.4. For Python 3/Renpy 8 the super calls
# can be simplified.
#
init python:
    class FsmTimer(Fsm):
        """
        Finite State Machine with ticks and count down timer.

        Ticks counts up and resets when the state changes.
        Timer counts down from a supplied value. When it reaches zero timerTrig
        is set and timerTrigger() is called.
        """

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self, stateNames=None):
            """
            Construct a finite state machine with timers and initial state 0.

            Optionally provide a renpy.store name of sequence of state names.
            This can be a list or a tuple of strings.

            :param stateNames: Optional store name of a sequence of state names
            """
            super(FsmTimer, self).__init__(stateNames)
            self._ticksM = 0
            self._timerM = 0
            self._timerTrigM = False


        # ---------------------------------------------------------------------
        # Timer methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def tick(self):
            """
            Register a clock tick.

            The ticks value is incremented.
            The timer value is decremented is it is positive.
            If it reaches zero then timerTrig is set and timerTriggered is called.
            """
            self._ticksM += 1
            if self._timerM > 0:
                self._timerM -= 1
                if self._timerM == 0:
                    self._timerTrigM = True
                    self.timerTriggered()

        def timerTriggered(self):
            """
            Called when timer reaches zero.

            Intended to be overloaded.
            """
            pass



        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def reset(self):
            """
            Reset to state zero and cleat ticks and timer.
            """
            super(FsmTimer, self).reset()
            self._ticksM = 0
            self._timerM = 0

        @Fsm.state.setter
        def state(self, value):
            """
            Set the state number.

            The state number cannot be None or negative.
            If a sequence of state names was provided the value must be a
            valid index.
            If the state changes as a result then reset the ticks counter.

            :param value: The new state number
            """
            if value is None:
                raise ValueError("State cannot be set to None.")
            if not isinstance(value, int):
                raise ValueError("State cannot be set to a non-integer value ({})".format(value))
            if value < 0:
                raise ValueError("State cannot be set to a negative value ({}).".format(value))
            if self._stateNamesM is not None:
                names = self._lookupNames()
                if value >= len(names):
                    raise ValueError("State cannot be set outside known states 0..{} ({}).".format(len(names)-1, value))
            # If state changes, reset ticks.
            if self._stateNumM != value:
                self._ticksM = 0
            self._stateNumM = value

        @property
        def ticks(self):
            """
            The number of ticks since the last state change.
            """
            return self._ticksM

        @property
        def timer(self):
            """
            The count down tick timer.
            """
            return self._timerM

        @timer.setter
        def timer(self, value):
            """
            Set the countdown timer and resets the triggered flag.

            :param value: The new value.
            """
            if value is None:
                raise ValueError("Timer cannot be set to None.")
            if not isinstance(value, int):
                raise ValueError("Timer cannot be set to a non-integer value ({})".format(value))
            if value < 0:
                raise ValueError("Timer cannot be set to a negative value ({}).".format(value))
            self._timerM = value
            self._timerTrigM = False

        @property
        def timerTrig(self):
            """
            Set when the count down tick timer reaches zero.
            """
            return self._timerTrigM

        @timerTrig.deleter
        def timerTrig(self):
            """
            Clear any timer trigger.
            """
            self._timerTrigM = False


        # ---------------------------------------------------------------------
        # Special methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __str__(self):
            """
            Generate a printable string describing the state.
            """
            names = self._lookupNames()
            if names is None:
                return "{} ticks={} timer={} trig={}".format(
                    self._stateNumM,
                    self._ticksM,
                    self._timerM,
                    self._timerTrigM\
                )
            return "{}:{} ticks={} timer={} trig={}".format(
                    self._stateNumM,
                    names[self._stateNumM],
                    self._ticksM,
                    self._timerM,
                    self._timerTrigM\
                )

# EoF

        