#


init python:
    class Phone:

        def __init__(self, homeApp, apps):
            self._homeAppM = homeApp
            self._appsM = apps
            # Init apps list.
            if not homeApp in apps:
                self._appsM.append(homeApp)
            # Init state.
            self._openM = False
            self._curAppM = None


        def open(self):
            # Ignore if already open.
            if self._openM:
                return
            # Select home screen if needed.
            if self._curAppM is None or not self._curAppM.isRunning():
                self.home()
            # Show and transition.
            renpy.show_screen('phoneScr', self)
            # Mark as open.
            self._openM = True

        def close(self):
            # Ignore if already closed.
            if not self._openM:
                return
            # Transition and hide
            renpy.hide_screen('phoneScr')
            # Close current app.
            if self._curAppM is not None:
                self._curAppM.stop(self)
                if not self._curAppM.isRunning():
                    self._curAppM = None
            # Mark as closed.
            self._openM = False

        def home(self):
            """
            Start the home application.
            """
            self.startApp(self._homeAppM)

        def startApp(self, app):
            """
            Start an application.

            Any current app is stopped, and the new app started.

            :param app:     the new application
            """
            if self._curAppM is not app:
                if self._curAppM is not None:
                    # Stop current app.
                    self._curAppM.stop(self)
                self._curAppM = app
            self._curAppM.start(self)



