def closest_power(base,num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
     
    
    exp = 0
    while num > base**exp:
        
        exp += 1
        
    if abs(base ** exp -num) < abs(base ** (exp-1) -num):
        return  exp 
    else:
        return  exp-1
        
closest_power(2, 192.0)
