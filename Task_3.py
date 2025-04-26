import random #use random library
factorial_number = random.randint(0,10) #give a range of numbers
compute = 1 #to store results for later
print("Random number is: " + str(factorial_number)) #show random number used
while 1 < factorial_number:
    compute *= factorial_number #main process occurance
    factorial_number -= 1 #reduce factorial number by 1
print("Factorial is: " + str(compute)) #output