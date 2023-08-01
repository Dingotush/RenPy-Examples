label exRndLru:
    $ renpy.dynamic('labelList', 'labelLru', 'lruStr')

    # Random label draw.
    #
    "Call random labels with lru list"
    $ labelList = ['alleyEmpty', 'alleyCat', 'alleyRat', 'alleyVomit']
    $ labelLru = []
    $ done = False
    while not done:
        call callRndLabelLru(labelList, labelLru, 2)
        $ lruStr = ", ".join(labelLru)
        menu:
            "Used list now: [lruStr]"
            "Again":
                pass
            "Done":
                $ done = True

    return