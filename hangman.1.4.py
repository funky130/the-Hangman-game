import random as rand
HANGMAN_ASCII_ART = """ 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = rand.randint(5,10)

print("\n\n\nWelcome to the game Hangman!" , HANGMAN_ASCII_ART,"\n\n\n", "this is your max tries: ", MAX_TRIES,"\n\n\n")

word = input("Enter your word: ")
word_length = len(word)
word_print = '- ' * word_length
print("\n", word_print, "\n")

old_letters_guessed = ['a', 'p', 'c', 'f']

def check_valid_input(letter_guessed, old_letters_guessed):
    """בודקת גם אם כבר השתמשו באות המופיעה  פונקציה שמקבלת אות ובודקת אם האות תקינה לפי התנאים הבאים: """
    letter_guessed = letter_guessed.lower()
    if (len(letter_guessed) > 1) or (letter_guessed.isalpha() == False) or (letter_guessed in old_letters_guessed) :
        return False
    else:
        return True


def add_to_list(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    old_letters_guessed.append(letter_guessed)
    return old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        add_to_list(letter_guessed, old_letters_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(old_letters_guessed))
        return False

letter_guessed = input("Enter your letter: ")

print(try_update_letter_guessed(letter_guessed , old_letters_guessed))

print(old_letters_guessed)




print("    x-------x")
print("""    x-------x
    |
    |
    |
    |
    |""")
print("""    x-------x
    |       |
    |       0
    |
    |
    |""")

print("""    x-------x
    |       |
    |       0
    |       |
    |
    |
""")

print("""    x-------x
    |       |
    |       0
    |      /|/
    |
    |""")

print("""    x-------x
    |       |
    |       0
    |      /|/
    |      /
    |""")

print("""    x-------x
    |       |
    |       0
    |      /|/
    |      / /
    |""")