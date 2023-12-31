#
# A single phone message.
#
init python:
    class PhoneMsg:

        # ---------------------------------------------------------------------
        # Constructor
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __init__(self, rx, what, imgSm=None, imgLg=None):
            self.rx = rx
            self.what = what
            self.imgSm = imgSm
            self.imgLg = imgLg

        # ---------------------------------------------------------------------
        # Accessors
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



        # ---------------------------------------------------------------------
        # Object methods
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        def __str__(self):
            direction = "rx" if self.rx else "tx"
            return "Post {} {} {} {}".format(direction, self.what, self.imgSm, self.imgLg)


        