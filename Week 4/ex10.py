numLow = int(input("Enter the low number: "))
numHigh = int(input("Enter the high number: "))
numRange = range(numLow, numHigh)

def FizzBuzz(x):
    for x in range(numLow, numHigh):
        if x%5 == 0 and x%3 == 0:
            print("FizzBuzz")
        elif x%5 == 0:
            print("Buzz")
        elif x%3 == 0:
            print("Fizz")
        else:
            print(x)

FizzBuzz(numRange)
