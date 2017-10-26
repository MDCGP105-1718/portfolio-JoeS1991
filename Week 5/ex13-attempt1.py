print("Welcome to Hangman.")
guessMax = int(input("How many attempts would you like? "))
print("Okay, start guessing!")
guessCount = 0
word = "Suffolk"
guesses = []

while guessCount < guessMax:
    guess = input("Pick a letter: ")
    guessCount += 1
    if guess in word.lower() or word.upper():
        print("This letter is in the word!")
        guesses.append(guess)
        print(f"Correct guesses so far: {guesses}")
    elif guess not in word:
        print("This letter is not in the word.")

#this code was from before we had the worksheet.
