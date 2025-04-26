import random #use random library
num = random.randint(0,12) #give range of random numbers
def factorial (num):
    if num == 0 or num == 1: #basecase
        return 1
    else:#recursive fumction
        return num *factorial(num - 1)
print("Factorial of " + str(num) + " is " + str(factorial(num)))#output