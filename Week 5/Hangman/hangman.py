# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if set(secret_word).issubset(letters_guessed): #google-fu led me to treating lists as sets and using set(set1).issubset(set2)
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    space = ['_ '] * len(secret_word)
    secret_word_list = list(secret_word)
    loops = 0
    for i in secret_word_list:
        if i in letters_guessed:
            loops += 1
            space.insert(loops-1,i + ' ')
            del space[loops]
            if loops == len(secret_word):
                return ''.join(space)

        else:
            loops += 1
            space.insert(loops-1,'_ ')
            del space[loops]
            if loops == len(secret_word):
                return ''.join(space)

def get_guessed_word_truefalse(secret_word, letters_guessed):
    secret_word_list = list(secret_word)
    for i in secret_word_list:
        if i in letters_guessed:
            return True
        else:
            return False


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for e in letters_guessed:
        if e in string.ascii_lowercase:
            alphabet.remove(e)
    return ''.join(sorted(alphabet))

secret_word = choose_word(wordlist)
#secret_word = "test"

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    hiddenGuesses = 0
    warnings = 3
    guessesMax = 6
    guessesCurrent = 0
    letters_guessed = []
    secret_word_len = len(secret_word)
    blanks = ['_ '] * len(secret_word)

    print(f"Welcome to Hangman, the word I am thinking of is {secret_word_len} characters long.")
    print(f"You have {guessesMax} guesses.")
    print(''.join(blanks))

    while guessesCurrent <= guessesMax:
        guess = str.lower(input("Guess a letter: "))
        guessesLeft = guessesMax - guessesCurrent
        available_letters = get_available_letters(letters_guessed)
        points = guessesLeft * len(set(secret_word))

        if is_word_guessed(secret_word,letters_guessed) == False:

            if str.isalpha(guess) and len(guess) == 1:
                letters_guessed.append(guess)

                if is_word_guessed(secret_word,letters_guessed) == True:
                    hiddenGuesses += 1
                    print("---------------------")
                    print(f"Well done, you guessed the word! It was '{secret_word}' and it took you {hiddenGuesses} guesses. You got {points} points!")
                    break

                if guess in secret_word:
                    print("Good guess: ", get_guessed_word(secret_word,letters_guessed))
                    hiddenGuesses += 1

                elif guess not in secret_word:
                    print("That letter is not in the word:", get_guessed_word(secret_word,letters_guessed))
                    guessesCurrent += 1
                    hiddenGuesses += 1

            else:
                if warnings > 0:
                    warnings -= 1
                    print(f"That is not a valid letter! You have {warnings} warnings left.")

                elif warnings <= 0:
                    guessesCurrent += 1
                    print("That is not a valid letter! You have no warnings left and are now losing guesses!")

            if guessesLeft > 1:
                print(f"You have {guessesLeft} guesses left.")
                print(f"Available letters: {available_letters}")
                print("---------------------")

            elif guessesLeft == 1:
                print("You have 1 guess left!")
                print(f"Available letters: {available_letters}")
                print("---------------------")

            else:
                print("---------------------")
                print(f"You have no guesses left! The word was '{secret_word}'.")
                break


hangman(secret_word)

# -------------------------------------------------------------------------
# Functions defined above, now attempting to write the code that executes them correctly.
