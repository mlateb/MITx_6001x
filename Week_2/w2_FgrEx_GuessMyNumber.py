secGuess = 42
lowVal = 0
higVal = 100

print("Please think of a number between 0 and 100!")

while True:


    secGuess = (higVal + lowVal)//2
    print ("Is your secret number "+ str(secGuess) +"?")
    
    userAns = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if userAns != 'h' and userAns != 'l' and userAns != 'c': 
    
        print ("Sorry, I did not understand your input.")
        

    else:
        if userAns == 'h':
            higVal = secGuess
        elif userAns == 'l':
            lowVal = secGuess
        else :
            userAns == 'c'
            print ("Game over. Your secret number was:", secGuess)

            break
