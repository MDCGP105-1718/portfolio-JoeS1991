numLow = int(input("Enter the low number: "))
numHigh = int(input("Enter the high number: "))

def Fizz(x):
    """
    Returns true if x divisible by 3
    """
    return x%3 == 0

def Buzz(x):
    """
    Returns true if x divisible by 5
    """
    return x%5 == 0

def FizzBuzz(x):
    """
    Returns true if x divisible by 3 and 5
    """
    return x%5 == 0 and x%3 == 0

for x in range(numLow, numHigh):
    if FizzBuzz(x) == True:
        print("FizzBuzz")
    elif Fizz(x) == True:
        print("Fizz")
    elif Buzz(x) == True:
        print("Buzz")
    else:
        print(x)
