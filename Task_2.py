import random #use random library
n = random.randint(1,1000) #give a range of numbers to be used
def EvenOdd(): #function for checking even or odd
    if n%2 == 0: #use modulus for calculation
        return 'even' 
    else:
        return 'odd'
print("random number: " + str(n) + " is " + EvenOdd()) #output