

define  fsmTimerStateNames = ('init', 'wait', 'done')
default fsmTimer = FsmTimer('fsmTimerStateNames')

label exFsmTimer:
    "Initial state: [fsmTimer]"

    $ fsmTimer.tick()
    "After tick: [fsmTimer]"

    $ fsmTimer.stateName = 'wait'
    $ fsmTimer.timer = 2
    "After stateName='wait' and timer=2: [fsmTimer]"

    while not fsmTimer.timerTrig:
        $ fsmTimer.tick()
        "After tick: [fsmTimer]"

    $ del fsmTimer.timerTrig
    "After del timerTrig: [fsmTimer]"

    $ fsmTimer.stateName = 'done'
    "After stateName='done': [fsmTimer]"

    "Done."
    $ fsmTimer.reset()
    return