label exPhoneSignal:
    $ renpy.dynamic('alex', 'apps', 'appHome', 'contacts', 'msgList', 'mom', 'momMsg', 'phone', 'sis', 'sisMsg')
    $ phone = Phone()
    $ me = phone.addContactOwner("Me")
    $ alex = phone.addContact("Alex")
    $ mom = phone.addContact("Mom")
    $ sis = phone.addContact("Sis")
    scene bg village
    $ phone.signal = 100
    $ phone.open()
    $ phone.closeLock=True
    "Phone reception here is rather tricky."
    $ phone.signal = 80
    "It seems to change for no reason."
    $ phone.signal = 40
    "I've only got to move a little and it's dropped."
    $ phone.signal = 60
    "A single step and it's back."
    $ phone.signal = 1
    "A pace the other way and there's almost nothing."
    $ phone.signal = 0
    "And now it's gone completely!"
    $ momMsg = phone.msgCharRx(mom)
    $ sisMsg = phone.msgCharRx(sis) 
    momMsg "While you're in town can you pick up some cheese?"
    momMsg "And some tomatoes?"
    sisMsg "As you're in town can you get some cake?
        I fancy a little celebration."
    "I hope no one tries to call or text me. I should probably go back to where
    the signal was stronger."
    $ phone.signal = 90
    "Time to check my messages..."
    "Done."
    $ phone.closeLock=False
    $ phone.close()
    hide screen phoneButtonScr
    pause 0.5
    scene black
    return