def f(a,b):
    
    return a+b


def dict_interdiff(d1,d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries 

    """

    
    inteDic = {}
    diffDic = {}
    
    #create an temporary iteration liste
    iterList = list(d1.keys())+list(d2.keys())
    #remove duplicates from temiterList
    
    for i in iterList:
        if iterList.count(i) >1:
            iterList.remove(i)
    #sort iterlist
    iterList.sort()

    ########################
    
    for i in iterList:
        if i in d2 and i in d1:
            
            inteDic[i] = f(d1[i],d2[i])

        else :
            if i in d1:
                diffDic[i] =  d1[i]
                
            else:
                diffDic[i] = d2[i]
    outputTuple = (inteDic,)+(diffDic,)
    return outputTuple

