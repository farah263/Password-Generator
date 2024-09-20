# Password_generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# letter + symbols + numbers
password = ""
print("Welcome to the 3Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you likein your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

for char in range (1, nr_letters + 1):
    password = random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)
print("".join(random.sample(password, len(password)))) # convert str to list and shuffle the list and convert back to str
