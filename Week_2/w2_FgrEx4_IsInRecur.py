def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len (aStr) == 0 :
        return False
    elif len(aStr) == 1 :
        if char == aStr :
            return True
        else:
            return False
    
    index = (len(aStr)//2)+1
    if len(aStr) % 2!= 0:

        if aStr[index] == char:
            return True

    elif aStr[index] > char:
        return isIn(char,aStr[0:index])
    else :
        return isIn(char,aStr[index:])
