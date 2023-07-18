
define  stateNames = ('init', 'first', 'second')
default fsm = Fsm('stateNames')

label exFsm:
    "Initial state: [fsm.state] [fsm.stateName]"

    "$ fsm.state = 1"
    $ fsm.state = 1
    "New state: [fsm.state] [fsm.stateName]"

    "$ fsm.state += 1"
    $ fsm.state += 1
    "New state: [fsm.state] [fsm.stateName]"

    "$ fsm.reset()"
    $ fsm.reset()
    "Reset state: [fsm.state] [fsm.stateName]"

    "$ fsm.stateName = 'second'"
    $ fsm.stateName = 'second'
    "New state: [fsm.state] [fsm.stateName]"
    $ fsm.reset()

    # These would all raise exceptions:
#   $ fsm.stateName = 'third'
#   $ fsm.state = 3
#   $ fsm.state = 'init'
#   $ fsm.state = None
#   $ fsm.state = 0.1
    "Done"
    return

