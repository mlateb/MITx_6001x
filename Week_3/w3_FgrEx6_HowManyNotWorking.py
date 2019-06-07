def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
      
    a = 0
    for key in aDict.keys():
        a += len(aDict[key]
    
    
    return a


animals = { 'd': ['donkey', 'dog', 'dingo'], 'c': ['coati'], 'b': ['baboon'], 'a': ['aardvark']}

how_many(animals)
