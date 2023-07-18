    #
    # Floating point examples.
    #
label exFlt:
    $ tmp = 0.1 + 0.1 + 0.1 == 0.3
    "0.1 + 0.1 + 0.1 == 0.3 [tmp]"

    $ tmp = 2.0 ** 53
    "2.0 ** 53 = [tmp:,f]"
    $ tmp += 1
    "2.0 ** 53 + 1 = [tmp:,f]"

    return