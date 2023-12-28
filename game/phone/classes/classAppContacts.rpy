#
# Phone home screen state.
#
init 1 python:
    class AppContacts(PhoneApp):
        def __init__(self):
            super().__init__('contacts', 'appContactsScr')