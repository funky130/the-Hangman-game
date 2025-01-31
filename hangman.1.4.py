import random as rand

second_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(second_list[1][0][1])                   
THE_CHOSEN_WARD =""

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

print(word_print)


guess = input("enter your guesses: ")
guess = guess.lower()

def is_valid_input(letter_guessed):
    """  פונקציה שמקבלת אות ובודקת אם האות תקינה לפי התנאים הבאים: """
    if len(letter_guessed) > 1 :
        return False
    elif letter_guessed.isalpha() == True:
        return False
    else:
        return True

print(is_valid_input(input("enter your guesses: ")))
    

guess_length = len(guess)


if guess_length > 1 and not guess.isalpha():
    print("E3")

elif guess_length > 1:
    print("E1")

elif not guess.isalpha():
    print("E2")



print(guess)






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