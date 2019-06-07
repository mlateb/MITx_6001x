def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bigestKey = ""
    bigestValue = 0
    for key in aDict.keys():
        if len(aDict[key])> bigestValue:
            bigestKey = key
            bigestValue = len(aDict[key])
    return bigestKey
