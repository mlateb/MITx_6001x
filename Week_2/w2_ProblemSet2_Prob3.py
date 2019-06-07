balance = 3329
annualInterestRate = 0.2


monthlyInterestRate = annualInterestRate / 12.0


balance1 = balance

lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0

while True:
    
    balance = balance1
    minimumMonthlyPayment = (upperBound + lowerBound)/2    
    month = 0

    while month < 12:
    
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

        month += 1
        
    if balance**2 < 0.01:
        print ("Lowest Payment:",round (minimumMonthlyPayment, 2))
        break
    elif balance > 0 :
        lowerBound = minimumMonthlyPayment
    else:
        upperBound = minimumMonthlyPayment
