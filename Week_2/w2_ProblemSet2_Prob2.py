
balance = 3329
annualInterestRate = 0.2


monthlyInterestRate = annualInterestRate / 12.0

minimumMonthlyPayment = 0
balance1 = balance
while True:
    
    balance = balance1
        
    month = 0

    while month < 12:
    
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

        month += 1
        
    if balance <= 0:
        print ("Lowest Payment:",minimumMonthlyPayment)
        break
    else :
        minimumMonthlyPayment += 10


