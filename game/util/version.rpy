    # Utilities for checking the running version of Python and RenPy.
    # Used occasionally in these examples to gate off code that won't work.
    # Not normally needed in a released Ren'Py game as it is packaged with
    # the required version of Ren'Py and Python.
    #
init python:

    def checkPyVersion(reqMajor, reqMinor):
        """
        Determine if a given or better version of Python is being used.

        :param reqMajor:    Required major version number.
        :param reqMinor:    Required minor version number.
        :return:            True if it is.
        """
        major = sys.version_info[0]
        minor = sys.version_info[1]
        # dbg("Python {}.{}".format(major, minor))
        return major > reqMajor or major == reqMajor and minor >= reqMinor

    def checkRenPyVersion(reqMajor, reqMinor):
        """
        Determine if a given or better version of RenPy is being used.

        :param reqMajor:    Required major version number.
        :param reqMinor:    Required minor version number.
        :return:            True if it is.
        """
        major = renpy.version_tuple[0]
        minor = renpy.version_tuple[1]
        # dbg("Ren'Py {}.{}".format(major, minor))
        return major > reqMajor or major == reqMajor and minor >= reqMinor
