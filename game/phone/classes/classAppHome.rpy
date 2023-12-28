#
# Phone home screen state.
#
init 1 python:
    class AppHome(PhoneApp):
        def __init__(self):
            super().__init__('home', 'appHomeScr')