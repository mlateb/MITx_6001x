def listFlaten(listX):
    if listX == []:
        return listX
    if type(listX[0])== list:
        return listFlaten(listX[0]) + listFlaten(s[1:])
    return listX[:1]+ listFlaten(lisX[1:])
        
        
def f(aList):
    
    bList = []
    for i in aList:
        
	if type(i) != list :
            return bList.append(aList[i])
        else:
            bList += f(aList)

    return bList
        
            
            
                    
