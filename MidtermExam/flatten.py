        
def f(aList):
    
    bList = []
    for i in aList:
        
	if type(i) != list :
            return bList.append(i)
        else:
            bList += f(aList)

    return bList
        
