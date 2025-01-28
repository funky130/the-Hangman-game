

import os # Please ignore this line
os.environ['PAGER'] = 'cat' # Please ignore this line


def func(num1, num2):
    """
    תוכנית שמקבלת שני מספרים ומחברת אותם"""
    return num1 + num2

def main():
    help(func)
    print(func(3, 4))


if __name__ == '__main__':
    main()




def chocolate_maker(small, big, x):

    big_bars = big * 5
    if(big_bars + small == x):
        return True
    else: False
    

def main():
    print(chocolate_maker(3, 1, 8))  # Output: True
    print(chocolate_maker(3, 1, 9))  # Output: False
    print(chocolate_maker(3, 2, 10)) # Output: True
    

if __name__ == "__main__":
    main()



def fix_age(age):
    if age >= 13 and age < 15 or age > 16 and age <= 19:
        return 0
    else:
        return age


def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)    

def main():
    print(filter_teens())           # Output: 0
    print(filter_teens(1, 2, 3))    # Output: 6
    print(filter_teens(2, 13, 1))   # Output: 3
    print(filter_teens(2, 1, 15))   # Output: 18
    

if __name__ == "__main__":
    main()







import calendar
date = input("Enter a date: ")

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])

x = int(calendar.weekday(year, month, day) + 1)

if x == 0:
    print("sunday")
elif x == 1:
    print("monday")
elif x == 2:
    print("shlysy")
elif x == 3:
    print("ravyiy")
elif x == 4:
    print("hamishy")
elif x == 5:
    print("shiy shiy")
elif x == 6:
    print("shabes")






def last_early(my_str):
    if my_str[-1] in my_str[0:-1].lower():
        return True
    else:
        return False

def main():
    print(last_early("happy birthday")) # True
    print(last_early("best of luck")) # False
    print(last_early("Wow")) # True
    print(last_early("X")) # False


if __name__ == "__main__":
    main()












temperature = str(input("Insert the temperature you would like to convert: "))

c_or_f = temperature[-1]

tamp = int(temperature[0:-1])

if c_or_f == 'f' or c_or_f == 'F':

    C = ( 5 * tamp - 160) / 9
    print(C, "C")

elif c_or_f == 'c' or c_or_f == 'C':

    F = ( 9 * tamp + 32 * 5) / 5

    print(F, "F")











user_input = input("Please enter a string: ")

length = len(user_input)

zoogy = (length % 2) == 0

x = int(length / 2)

first_half = user_input[:x]
second_half = user_input[x:]

print(first_half + second_half.upper())
