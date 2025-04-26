import random
n = random.randint(1,1000)
def EvenOdd():
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'
print("random number: " + str(n) + " is " + EvenOdd())