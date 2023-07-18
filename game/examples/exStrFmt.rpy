    #
    # New string formatting.
    #
label exStrFmt:
#    python:
#        tmp = """
#        This is a python string block with "quoted text"
#        that goes over several lines.
#
#        Including blank ones.
#        """
#    "[tmp]"

    $ name = "Jim"
    $ age = 32
    $ tmp = "My name is {} and I am {} years old.".format(name, age)
    "[tmp]"

    $ tmp = "My name is {} and I am {age} years old.".format(name, age=24)
    "[tmp]"

    $ massKg = 56.789
    $ tmp = "I weigh {:.1f} kilos. That's {:.0f} pounds.".format(massKg, massKg*2.2)
    "[tmp]"

    $ tm = "\N{TRADE MARK SIGN}"
    $ tmp = "Symbol {0} decimal {1:d} hex {1:#x}.".format(tm, ord(tm))
    "[tmp]"

    $ aries = "\N{ARIES}"
    $ tmp = "My name is {name}. I'm an {zodiac} {symbol}.".format(name="Shiela", zodiac="Aries", symbol=aries)
    "[tmp]"

    python:
        book = (
            "on interactive storytelling",
            "Chris Crawford",
            "978-0-321-27890-8",
            "New Riders",
        )
    $ tmp = "'{0[0]}' by {0[1]}\nISBN: {0[2]}".format(book)
    "[tmp]"

#    $ tmp = "Health: {0.hp}/{0.hpMax}".format(pcStats)
#    "[tmp]"
    return