def polysum(n,s):
    '''
    input: n, number of polygon sides
           s, length of each side
    output: sumVa, sum of the area and square of the perimeter of a regular polygon
                
    '''
    # importing the math module
    import math
    
    # computing area of polygone using 2 math module
    # math.tan() and math.pi
    area = (0.25*n*s**2)/math.tan(math.pi/n)

    #computing the perimeter of a polygone
    peri = n*s

    #computing the sum of the area, plus the square of the perimeter
    sumVa = area + peri**2

    # returning the value of sumVa rounded to 4 decimal places
    #using the module round()
    return round(sumVa,4)
