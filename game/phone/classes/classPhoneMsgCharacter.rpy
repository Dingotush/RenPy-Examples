#
#
#
init python:
    class PhoneMsgCharacter:

        def __init__(self, phone, contact, rx):
            """
            Initialise a phone message character.

            :param phone:       The phone
            :param contact:     The phone contact
            :param rx:          True to receive these messages
            """
            self._phoneM = phone
            self._contactM = contact
            self._rxM = rx
            return


        def __str__(self):
            who = self._contactM._whoM
            result = renpy.substitutions.substitute(who)[0]
            if PY2:
                result = result.encode("utf-8")
            return result
            


        def __call__(self, what, interact=True, *args, **kwargs):
            """
            Say something on the phone message system.

            See: renpy/exports.py:say(who, what, *args, **kwargs)

            :param what:
            :param args:
            :param kwargs:
            """
            post = (self._rxM, what)
            self._contactM._msgHistM.append(post)
            self._contactM._unreadM += 1
            
            if interact:
                renpy.call_screen("phoneSayScr")

            # ADVCharacter.__call__
            #    ADVCharacter.do_display(who, what, cb_args, dtt=dtt, **display_args)
            #       display_say(who, what, self.do_show, **display_args)
            # do_show rets ADVCharacter.show_function