import random as rand

HANGMAN_PHOTOS = {"photo1" : """    x-------x""", "photo2" : """    x-------x
    |
    |
    |
    |
    |""" , "photo3" : """    x-------x
    |       |
    |       0
    |
    |
    |""" , "photo4" : """    x-------x
    |       |
    |       0
    |       |
    |
    |
""" , "photo5" : """    x-------x
    |       |
    |       0
    |      /|/
    |
    |""" , "photo6" : """    x-------x
    |       |
    |       0
    |      /|/
    |      /
    |""", "photo7" : """    x-------x
    |       |
    |       0
    |      /|/
    |      / /
    |"""}

HANGMAN_ASCII_ART = """ 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

num_of_tries = rand.randint(5,10)

print("\n\n\nWelcome to the game Hangman!" , HANGMAN_ASCII_ART,"\n\n\n", "this is your max tries: ", num_of_tries,"\n\n\n")

secret_word = input("Enter your secret_word: ")
word_length = len(secret_word)
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

print(old_letters_guessed, "\n")
def show_hidden_word(secret_word, old_letters_guessed):
    word_print = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_print += letter + " "
        else:
            word_print += "_ "
    return word_print.strip()

print(show_hidden_word(secret_word, old_letters_guessed)) 


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    else: return True

print(check_win("pac", old_letters_guessed))



def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS["photo" + str(num_of_tries)])


print(print_hangman(7))



def choose_word(file_path, index):
    file = open(file_path, 'r')
    words = file.read().split()
    file.close()
    words = set(words)
    return (len(words), words[(index - 1) % len(words)])

print(choose_word("file1.txt", 3))
 


