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
            :param rx:          True for phone owner to receive these messages
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
            # Prepare the post.
            post = PhoneMsg(self._rxM, what)

            # Powered off or no signal?
            if not phone.hasSignal:
                self._contactM.msgQueue(post)
                interact = False
            else:
                # New unseen message.
                self._contactM.msgUnseen(post)
            
            if interact:
                renpy.call_screen("phoneSayScr")

            # ADVCharacter.__call__
            #    ADVCharacter.do_display(who, what, cb_args, dtt=dtt, **display_args)
            #       display_say(who, what, self.do_show, **display_args)
            # do_show rets ADVCharacter.show_function

        def openMsgSystem(self, appLock=True):
            """
            Open the phone to message this contact.
            May not succeed if the phone is without power, signal.

            :appLock:           Lock the application, default True
            :return:            True if the message screen is now open
            """
            if not self._phoneM.hasSignal:
                return False
            self._phoneM.appLock = appLock
            if not self._phoneM.isOpen:
                print("openMsgSystem: phoneOpen")
                self._phoneM.open()
                renpy.pause(1.5)
            if self._phoneM.app._nameM == 'msgDx':
                if self._phoneM.app._contactM == self._contactM:
                    print("openMsgSystem: on msgDx for correct contact")
                    return True
                print("openMsgSystem: on msgDx for {}. Going back".format(self._phoneM.app._contactM._whoM))
                self._phoneM.app.back(self._phoneM)
                renpy.pause(1.2)
            if self._phoneM.app._nameM != 'msgList':
                print("openMsgSystem: opening msgList")
                self._phoneM.startApp('msgList')
                renpy.pause(1.2)
            print("openMsgSystem: opening msgDx for {}".format(self._contactM._whoM))
            self._phoneM.startApp('msgDx', self._phoneM.app, self._contactM)
            renpy.pause(1.2)
            return True

        def closeMsgSystem(self):
            self._phoneM.appLock = False
            self._phoneM.close()

            