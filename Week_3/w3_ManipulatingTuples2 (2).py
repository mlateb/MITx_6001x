def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    returnTup = ()
    i = 0
    for i in range len(aTup) :
        
        returnTup += (aTup[i],)
        i += 2
        print(i)
   
        return returnTup
