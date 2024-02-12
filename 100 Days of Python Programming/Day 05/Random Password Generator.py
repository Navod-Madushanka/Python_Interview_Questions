import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '\"', ',', '.', '/', '<', '>', '?']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcome to the Random Password Generator!")
letter_count = int(input("How many letters would you like in your password? \n"))
symbol_count = int(input("How many symbols would you like in your Password? \n"))
number_count = int(input("How many numbers would you like in your Password? \n"))

characters = ""

for n in range(0, letter_count):
    random_index = random.randint(0, len(letters) - 1)
    characters += letters[random_index]

for n in range(0, symbol_count):
    random_index = random.randint(0, len(symbols) - 1)
    characters += symbols[random_index]

for n in range(0, number_count):
    random_index = random.randint(0, len(numbers) - 1)
    characters += str(numbers[random_index])


password = ""
index_array =[]

for char_index in range(0, len(characters)):
    random_index = random.randint(0,len(characters) - 1)
    if random_index not in index_array:
        password += characters[random_index];
        index_array.append(random_index)


print(password)