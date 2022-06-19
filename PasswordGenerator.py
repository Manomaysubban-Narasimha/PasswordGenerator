# @author Manomay Subban Narasimha
# @version 2022-06-18
# Python 3.9.7
"""
Description: A program that generates a strong password (with random order)
by taking into account the number of letters, numbers, and symbols that 
the user would like to have in their password. 
"""
#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n")) 
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

password = ''

for i in range(num_of_letters):
    password += random.choice(letters)

for j in range(num_of_symbols):
    password += random.choice(symbols)

for k in range(num_of_numbers):
    password += random.choice(numbers)

used_indices = set()
strong_password = ''

while len(strong_password) < len(password):
    index = random.randint(0, len(password) - 1)
    if index not in used_indices:
        strong_password += password[index]
        used_indices.add(index)

print(f"Your password is {strong_password}")
    


    
