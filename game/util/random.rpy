    #
    # Random number utilities.
    #
init python:
    def rndProb(pTrue=0.5):
        """
        Generate a random boolean result with a given probability of True.

        :param pTrue: likelihood of a True result. Default half the time.
        """
        return renpy.random.random() < pTrue



    def rndPercent(pctTrue=50.0):
        """
        Generate a random boolean result with a given percentage of True.

        :param pctTrue: percentage of a True results. Default 50%.
        """
        return rndProb(pctTrue / 100.0)



    def rollDice(sides=6, rolls=1, add=0):
        """
        Sum a number of dice rolls.

        :param sides:   The number of sides on each dice. Default six.
        :param rolls:   How many rolls to make. Default one.
        :param add:     Any additional number to add to the total. Default zero.
        """
        result = add
        for roll in range(rolls):
            result += renpy.random.randint(1, sides)
        return result



    def rndPickLru(optionsList, usedList, usedDepth=1):
        """
        Pick from a list, but avoid recently used options.

        :param optionsList: List of options to pick from.
        :param usedList:    List of recently used options.
        :param usedDepth:   How many used options to ignore.
        """
        if usedList is None:
            raise ValueError("usedList cannot be None")
        if not optionsList:
            return None
        #
        # Make a copy of the options list.
        #
        workingList = optionsList.copy()
        #
        # Remove options that have been used recently.
        # Stop if only one option is left.
        #
        for used in usedList:
            if len(workingList) <= 1:
                break
            if used in workingList:
                workingList.remove(used)
        #
        # Pick one of the remaining options.
        #
        result = renpy.random.choice(workingList)
        #
        # Add the pick to the head of the used list.
        #
        if result in usedList:
            usedList.remove(result)
        elif len(usedList) >= usedDepth:
            usedList.pop()
        usedList.insert(0, result)

        return result


    # Call one of the labels from the provided list of labels.
    # Optionally a list of weights can be provided, one per label.
    #
label callRndLabel(listLabels, listWeights=None):
    $ renpy.dynamic('pick')
    $ pick = renpy.random.choices(listLabels, weights=listWeights)[0]
    if renpy.has_label(pick):
        call expression pick from call_rnd_label_dyn
    else:
        dbg "In callRndLabel: label [pick] does not exist."
    return



    # Call one of the labels from a deck of labels.
    # Add the called label to the discard list.
    # Recycle the doscrad list when the draw list is empty.
    #
label callRndLabelDeck(drawList, discardList):
    $ renpy.dynamic('pick')
    if not drawList:
        $ drawList.extend(discardList)
        $ discardList.clear()
    $ pick = renpy.random.choice(drawList)
    $ drawList.remove(pick)
    $ discardList.append(pick)
    if renpy.has_label(pick):
        call expression pick from call_rnd_label_deck_dyn
    else:
        dbg "In callRndLabelDeck: label [pick] does not exist."
    return



    # Call one of the labels from the provided list of labels, avoiding
    # recently used ones.
    #
label callRndLabelLru(labelList, usedList, usedDepth=1):
    $ renpy.dynamic('pick')
    $ pick = rndPickLru(labelList, usedList, usedDepth)
    if renpy.has_label(pick):
        call expression pick from call_rnd_label_lru_dyn
    else:
        dbg "In callRndLabelLru: label [pick] does not exist."
    return


