

default pcMoney = 9808

label exDollarsCents:
    $ dollars, cents = divmod(pcMoney, 100)
    "I have $[dollars:n].[cents:0=2]."

    $ dollars, cents = divmod(pcMoney, 100)
    if dollars:
        if not cents:
            "I have [dollars] dollars."
        elif cents == 1:
            "I have [dollars] dollars and one cent."
        else:
            "I have [dollars] dollars and [cents] cents."
    else:
        if not cents:
            "I have no money."
        elif cents == 1:
            "I have just one cent."
        else:
            "I have [cents] cents."

    $ pcMoney = 7654
    python:
        sp, cp = divmod(pcMoney, 10)
        gp, sp = divmod(sp, 10)
        pp, gp = divmod(gp, 10)
    "[pp]pp, [gp]gp, [sp]sp, [cp]cp"

    $ pcMoney = 2797
    python:
        dd, qp = divmod(pcMoney, 4)
        ss, dd = divmod(dd, 12)
        ll, ss = divmod(ss, 20)
        qf = (
            "",
            "\N{VULGAR FRACTION ONE QUARTER}",
            "\N{VULGAR FRACTION ONE HALF}",
            "\N{VULGAR FRACTION THREE QUARTERS}"
        )[qp]
    "\u00A3[ll]/[ss]/[dd][qf]"
    return