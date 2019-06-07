def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """

    incrTem = []
    incrFin = []
    decrTem = []
    decrFin = []
    i = 0
    while i < len(L):
        
        if incrTem == []:
            incrTem.append(L[i])
            i += 1
        elif L[i] >= L[i-1]:
            incrTem.append(L[i])
            i += 1
        else:
            incrTem = []
            
        if len(incrTem) > len(incrFin):
            incrFin = incrTem
            j1=i-len(incrTem)
    i = 0      
    while i < len(L):
        
        if decrTem == []:
            decrTem.append(L[i])
            i += 1
        elif L[i] <= L[i-1]:
            decrTem.append(L[i])
            i += 1
        else:
            decrTem = []
            
        if len(decrTem) > len(decrFin):
            decrFin = decrTem
            j2=i-len(decrTem)
    if len(incrFin) > len(decrFin) :
        return sum(incrFin)
    elif len(incrFin) < len(decrFin):
        return sum(decrFin)
    else:
        if len(incrFin) == len(decrFin):
            if j1 < j2:
                return sum(incrFin)
            else:
                return sum(decrFin)    
