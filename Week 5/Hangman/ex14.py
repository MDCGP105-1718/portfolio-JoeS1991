import string
secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']

def is_word_guessed(secret_word,letters_guessed):
    if set(secret_word).issubset(letters_guessed): #google-fu led me to treating lists as sets and using set(set1).issubset(set2)
        return True
    else:
        return False


def get_guessed_word(secret_word,letters_guessed):
    space = ['_ '] * len(secret_word)
    secret_word_list = list(secret_word)
    loops = 0
    for i in secret_word_list:
        if i in letters_guessed:
            loops += 1
            space.insert(loops-1,i + '')
            del space[loops]
            if loops == len(secret_word):
                return ''.join(space)
        else:
            loops += 1
            space.insert(loops-1,'_ ')
            del space[loops]
            if loops == len(secret_word):
                return ''.join(space)

def get_available_letters(letters_guessed):
    alphabet = list(string.ascii_lowercase)
    for e in letters_guessed:
        if e in string.ascii_lowercase:
            alphabet.remove(e)
    return ''.join(sorted(alphabet))

print(get_available_letters(letters_guessed))
