import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '=']

print("Welcome to PassBuddy, a free-to-use password generator.")

num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

letters_counter = 0
symbols_counter = 0
number_counter = 0

letters_id = 0
symbols_id = 1
numbers_id = 2

total_chars = num_of_letters + num_of_symbols + num_of_numbers

password = ""

for i in range(0, total_chars):
    current_type = random.randint(0, 2)
    print(i, current_type)

    # this area needs work - works for same amounts of chars (i.e. 3 letters, 3 symbols, 3 numbers) but not varying values
    if current_type == 0 and (letters_counter < num_of_letters):
        char_to_add = letters[random.randint(0, len(letters) - 1)]
        password = password + char_to_add
        letters_counter += 1
    else:
        current_type = 1

    if current_type == 1 and (symbols_counter < num_of_symbols):
        char_to_add = symbols[random.randint(0, len(symbols) - 1)]
        password = password + char_to_add
        symbols_counter += 1
    else:
        current_type = 2

    if current_type == 2 and (number_counter < num_of_numbers):
        char_to_add = numbers[random.randint(0, len(numbers) - 1)]
        password = password + char_to_add
        number_counter += 1
    else:
        current_type = 0

print(password)
print(letters_counter)
print(number_counter)
print(symbols_counter)