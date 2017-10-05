name = input("What is your name?" + " ") #I have put spaces after each input so that it looks correct when running on PowerShell.
age = int(input("What is your age?" + " "))
height = int(input("What is your height in cm?" + " "))
weight = int(input("What is your weight in kg?" + " "))
eyeColour = input("What colour are your eyes?" + " ").lower() #A bit of googling let me find that you can add .lower() to an input to have it defined in lower case regardless of what the user types.
hairColour = input("What colour is your hair?" + " ").lower()

#print(f"You are called {name}, you are {age} years old, you are {height}cm tall, you weigh {weight}kg, your eyes are {eyeColour}, and you have {hairColour} hair.")
#I had the line above here just to test that my inputs were working correctly. I have commented it out as it's very basic.

if weight > 100:
    print("You are very heavy. Must be muscles...")
elif weight < 40:
    print("You are very light.")
else:
    print("You are an average weight.")

if age > 65:
    print("You are elderly.")
elif age < 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

if height >= 182:
    print("You are tall, over 6 feet!")
elif height <= 152:
    print("You are short, under 5 feet!")
else:
    print("You are an average height.")
