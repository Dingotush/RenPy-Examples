    #
    # Old sprintf style formating.
    #
label exOldStrFmt:
    $ name = "Fred"
    $ tmp = "My name is %s." % name
    "[tmp]"

    $ name = "Fred"
    $ age = 21
    $ tmp = "My name is %s and I am %d years old." % (name, age)
    "[tmp]"

    $ name = "Fred"
    $ age = 21
    $ params = {'name': name, 'age': age}
    $ tmp = "My name is %(name)s and I am %(age)d years old." % params
    "[tmp]"  

    
    return