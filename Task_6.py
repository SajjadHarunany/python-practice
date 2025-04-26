import random #use random library
num = random.randint(1000, 999999) #give a range of numbers
def sum_of_digits(num): #initialize function
    if num == 0: #basecase
        return 0
    else: 
        return (num % 10) + sum_of_digits (num//10) #calculate answer using recursion
print("Random number generated: " + str(num)) #show number being used
print("Sum of the digits: " + str(sum_of_digits(num))) #output