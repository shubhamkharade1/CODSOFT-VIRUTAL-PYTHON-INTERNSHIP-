import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '?', '.', '<', '>', '/', ':', ';']

print("-----Password Generator-----")

num_lowercase_letters = int(input("No. of lowercase letters you want in password: "))
num_uppercase_letters = int(input("No. of uppercase letters you want in password: "))
num_numbers = int(input("No. of numbers you want in password: "))
num_symbols = int(input("No. of symbols you want in password: "))

password_list = []

for _ in range(num_lowercase_letters):
    password_list.append(random.choice(lowercase_letters))

for _ in range(num_uppercase_letters):
    password_list.append(random.choice(uppercase_letters))

for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

generated_password = "".join(password_list)

print("Generated password is:", generated_password)
