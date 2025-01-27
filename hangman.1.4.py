import random as rand

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
print("Welcome to the game Hangman!" , HANGMAN_ASCII_ART,"\n", MAX_TRIES,"\n\n\n\n")

word = input("Enter your word: ")

word_length = len(word)

word_print = '- ' * word_length

print(word_print)

guess = input("enter your guesses: ")
guess = guess.lower()

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