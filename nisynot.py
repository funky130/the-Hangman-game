import calendar







def is_greater(my_list, n):
    new_list = []
    for num in my_list:
        if num > n: 
            new_list.append(num)

    return new_list

result = is_greater([1, 30, 25, 60, 27, 28], 5)
print(result)

def longest_string(strings):
    if not strings:
        return None
    return max(strings, key=len)
    
my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(longest_string(my_list))  # Output: "beryllium"





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
