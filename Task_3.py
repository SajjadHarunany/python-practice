import random
factorial_number = random.randint(0,10)
compute = 1
print("Random number is: " + str(factorial_number))
while 1 < factorial_number:
    compute *= factorial_number
    factorial_number -= 1
print("Factorial is: " + str(compute))