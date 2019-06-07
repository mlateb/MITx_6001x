B = [4, 5, 6]
A = [1, 2, 3]
def dotProduct(listA,listB):
    sumPairProd = 0
    
    for index in range(len(listA)):
        sumPairProd += listA[index]*listB[index]
    return sumPairProd
