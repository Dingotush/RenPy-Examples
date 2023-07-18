define  dbg = Character("Debug")        # The voice of debug

default debugLabels = False             # Set True for dbgLabel to say debug lines

init python:

    def dbgLabel(gLbl, lLbl=None, sfmt=None, *args, **kwargs):
        """
        Output a debug say statement if debugLabels is True.

        :param gLbl:    Global label name.
        :param lLbl:    Local label name, default None.
        :param sfmt:    Format string, default None.
        :param args:    Args passed to sfmt.format.
        :param kwargs:  Keyword args passed to sfmt.format.
        """
        if not debugLabels:
            return
        msg = "Label " + gLbl
        if lLbl is not None:
            msg += '.' + lLbl
        if sfmt is not None:
            msg += ": " + sfmt.format(*args, **kwargs)
        dbg(msg)