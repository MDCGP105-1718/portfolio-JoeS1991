from random import randint

guess = int(input("Guess the number: "))
guesses = 0
num = randint(1,100)

def guessCheck(x):
    if x > num:
        print("Lower.")
    elif x < num:
        print("Higher.")

while guess != num:
        guessCheck(guess)
        guesses += 1
        guess = int(input("Try again: "))

if guess == num:
    print(f"Correct! The number was {num} and it took you {guesses} guesses.")
