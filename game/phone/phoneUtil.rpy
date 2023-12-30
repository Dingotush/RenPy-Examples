init python:

    def pauseInNewContext(delay=None, *args, **kwargs):
        """
        See: https://www.renpy.org/doc/html/label.html#renpy.invoke_in_new_context
        See: https://www.renpy.org/doc/html/statement_equivalents.html#renpy.pause
        See: renpy/exports.py:pause()
        """
        return renpy.invoke_in_new_context(renpy.pause, delay, *args, **kwargs)