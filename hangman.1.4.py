import random as rand

HANGMAN_PHOTOS = {"photo1" : """    x-------x""", "photo2" : """   x-------x
    |
    |
    |
    |
    |""" , "photo3" : """   x-------x
    |       |
    |       0
    |
    |
    |""" , "photo4" : """   x-------x
    |       |
    |       0
    |       |
    |
    |
""" , "photo5" : r"""   x-------x
    |       |
    |       0
    |      /|\
    |
    |""" , "photo6" : r"""   x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""", "photo7" : r"""   x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""}

HANGMAN_ASCII_ART = r""" 
  _    _                                         
 | |  | |                                            x-------x
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __      |       |
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \     |       0
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |    |      /|\
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|    |      / \
                      __/ |                          |
                     |___/"""

MAX_TRIES = rand.randint(5,7)

def word_shadow(secret_word):
    return "_ " * len(secret_word)


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
    """משתמשת הפונקציה check_valid_input כדי לדעת אם התו תקין ולא ניחשו אותו בעבר או התו אינו תקין ו/או נמצא כבר ברשימת הניחושים.
    אם התו איננו תקין או שכבר ניחשו את התו בעבר, הפונקציה מדפיסה את התו X (כאות גדולה), 
    מתחתיו את רשימת האותיות שכבר נוחשו ומחזירה שקר. אם התו תקין ולא ניחשו אותו בעבר - הפונקציה מוסיפה את התו לרשימת הניחושים ומחזירה אמת."""
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        add_to_list(letter_guessed, old_letters_guessed)
        return True
    else:
        print("\nX")
        print(" -> ".join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """ זאת פונקציה שמחזירה מחרוזת אשר מורכבת מאותיות ומקווים תחתונים.
      המחרוזת מציגה את האותיות מתוך הרשימה old_letters_guessed שנמצאות במחרוזת secret_word במיקומן המתאים,
        ואת שאר האותיות במחרוזת (אותן השחקן טרם ניחש) כקווים תחתונים."""
    word_print = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_print += letter + " "
        else:
            word_print += "_ "
    return word_print.strip()


def check_win(secret_word, old_letters_guessed):
    """זאת פונקציה בוליאנית שמחזירה אמת אם כל האותיות שמרכיבות את המילה הסודית נכללות ברשימת האותיות שהמשתמש ניחש. אחרת, הפונקציה מחזירה שקר."""
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    else: return True


def print_hangman(num_of_tries):
    print(f"\n{ HANGMAN_PHOTOS["photo" + str(num_of_tries)] }\n")
    if(num_of_tries > MAX_TRIES):
        print("error no more photos left :(")


def choose_word(file_path, index):
    """הפונקציה מקבלת כפרמטרים: מחרוזת המייצגת נתיב לקובץ טקסט המכיל מילים מופרדות ברווחים,
      ומספר שלם המייצג מיקום של מילה מסוימת בקובץ.
    הפונקציה מחזירה טאפל המורכב משני איברים בסדר הבא:
      (1) מספר המילים השונות בקובץ (2) מילה במיקום שהתקבל כארגומנט לפונקציה (index)."""
    file = open(file_path, 'r')
    words = file.read().split()
    file.close()
    words_new = list(dict.fromkeys(words))
    return  words_new[(index - 1)]

 
def main():
    old_letters_guessed = []
    num_of_tries = 0
    num_of_overall_tries = 0

    print("\n\nWelcome to the game Hangman!" , HANGMAN_ASCII_ART,"\n\n\n", "this is your max tries: ", MAX_TRIES,"\n\n\n")
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    print("\nok, lets start the game!\n")
    print_hangman(1)  # Call print_hangman directly
    secret_word = str(choose_word(file_path, index))
    print("\nthis is your secret word!!!\n", word_shadow(secret_word), "\n")

    while(num_of_tries <= MAX_TRIES):
        letter_guessed = input("\nEnter your letter: ")
        num_of_overall_tries += 1
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if check_win(secret_word,old_letters_guessed) == True:
            print(f"\nyou win!!! \n\nit took you {num_of_overall_tries} tries. this is your secret word: {secret_word}\n")
            break
        elif(letter_guessed.lower() in secret_word ):
            print(f"correct! {show_hidden_word(secret_word, old_letters_guessed)} ")
        else:
            num_of_tries += 1
            print_hangman(num_of_tries)
            if(num_of_tries == MAX_TRIES):
                print(f"you lose :(\nthis was the secret word: {secret_word} \ntry again next time!!")
                break
            print(f"not correct  :( \nold letters guessed: {old_letters_guessed} \n{show_hidden_word(secret_word, old_letters_guessed)}")
            

    

if __name__ == "__main__":
    main()