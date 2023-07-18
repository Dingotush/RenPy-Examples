#
# Finite State Machine.
#
default debugFsm = False

init python:
    class Fsm(object):
        """
        Basic state machine.

        State is held as a non-negative integer (0..n-1).
        An instance can optionally be supplied with a sequence of names for each state.
        If a sequence is provided the state is limited to only those states.

        Declaration:
        define  stateNames = ('init', 'first', 'second',)
        default state = Fsm('stateNames')
        """

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self, stateNames=None):
            """
            Construct a basic finite state machine with initial state 0.

            Optionally provide a renpy.store name of sequence of state names.
            This can be a list or a tuple of strings.

            :param stateNames: Optional store name of a sequence of state names
            """
            self._stateNumM = 0
            self._stateNamesM = stateNames



        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def reset(self):
            """
            Reset to state zero.
            """
            self.state = 0



        @property
        def state(self):
            """
            The state number which is a non-negative integer.
            """
            return self._stateNumM



        @state.setter
        def state(self, value):
            """
            Set the state number.

            The state number cannot be None or negative.
            If a sequence of state names was provided the value must be a
            valid index.

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
            self._stateNumM = value
            if debugFsm:
                if names is not None:
                    dbg("{}.state={}:{}".format(self.__class__.__name__, value, names[value]))
                else:
                    dbg("{}.state={}".format(self.__class__.__name__, value))

        @property
        def stateName(self):
            """
            The state name corresponding to the current state.
            """
            names = self._lookupNames()
            if names is None:
                return str(self._stateNumM)
            return names[self._stateNumM]

        @stateName.setter
        def stateName(self, value):
            """
            Set the state by name.

            Only valid if a sequence of state names was provided.

            :param value: The new state name
            """
            names = self._lookupNames()
            if names is None:
                raise ValueError("State names cannot be used without first providing a list of states ({}).".format(value))
            if value not in names:
                raise ValueError("State '{}' is not a valid state name.".format(value))
            self.state = names.index(value)


        
        def stateNumber(self, value):
            """
            Get the state number for a given state name.

            :param value:   A state name
            :return:        The state number
            """
            names = self._lookupNames()
            if names is None:
                raise ValueError("State names cannot be used without first providing a list of states ({}).".format(value))
            if value not in names:
                raise ValueError("State '{}' is not a valid state name.".format(value))
            return names.index(value)


        # ---------------------------------------------------------------------
        # Special methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __bool__(self):
            """
            Determine if the state has advanced beyond the reset state 0.

            :return: True if not in the initial state
            """
            return self._stateNumM != 0

        __non_zero__ = __bool__

        def __str__(self):
            """
            Generate a printable string describing the state.

            :return: A printable state name or number
            """
            names = self._lookupNames()
            if names is None:
                return str(self._stateNumM)
            return "{}:{}".format(self._stateNumM, names[self._stateNumM])



        # ---------------------------------------------------------------------
        # Private methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def _lookupNames(self):
            """
            Retrieve the sequence of state names from the renpy store.

            :return: The state name sequence, or None if not provided or available
            """
            if self._stateNamesM is None:
                return None
            return getattr(renpy.store, self._stateNamesM, None)

# EoF




        

