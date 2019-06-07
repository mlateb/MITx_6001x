def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    nmbrAll = 0
    for values in aDict.values():
        if len(values) == 0:
            nmbrAll += 0
        elif len(values)== 1:
            nmbrAll += 1
        else:
            nmbrAll += how_many(values)
            
    return nmbrAll


animals = { 'd': ['donkey', 'dog', 'dingo'], 'c': ['coati'], 'b': ['baboon'], 'a': ['aardvark']}

how_many(animals)
