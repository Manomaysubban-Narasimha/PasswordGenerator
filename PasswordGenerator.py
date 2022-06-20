# Author: Manomay Subban Narasimha
# Date: 2022-06-18
# Python 3.9.7
"""
Description: A program that generates a strong password (with random order)
by taking into account the number of letters, numbers, and symbols that 
the user would like to have in their password.
Time complexity: O(n) where n is the total number of characters within the password.
Space complexity: O(n) where n is the total number of characters within the password.
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

password = list()

'''Python's random module has the function choice(seq) which takes the
amount of time that it takes to access an element from the sequence passed
as the argument. In this case, the sequence would be a list, and it takes
constant time to access an element at any index within a list, so random
module's choice(seq) function would also take O(1) time to execute.'''

for i in range(num_of_letters):
    password += random.choice(letters)

for j in range(num_of_symbols):
    password += random.choice(symbols)

for k in range(num_of_numbers):
    password += random.choice(numbers)

'''Python's random module makes use of the Fisher-Yates shuffle algorithm
which takes linear time to implement the shuffle() function within
the random module. Thus, the shuffle(list) function would take O(n)
time where n is the length of the list'''
random.shuffle(password)

strong_password = ''

for char in password:
    strong_password += char

print(f"Your password is {strong_password}")
    
'''
Sample output:

Welcome to the PyPassword Generator!
How many letters would you like in your password?
6
How many symbols would you like?
5
How many numbers would you like?
4
Your password is %468$Wh%7b+h%dS
'''

    
