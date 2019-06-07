balance = 92
annualInterestRate = 0.2
monthlyPaymentRate = 0.08


monthlyInterestRate = annualInterestRate / 12.0


month = 0

while month < 12:
    
    minimumMonthlyPayment = monthlyPaymentRate * balance
    
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    month += 1
     

print ("Remaining balance:",round (balance, 2)) 
