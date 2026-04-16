import random

def length():
    while True:
        try:
            length = int(input("How Long Do You Want The Password To Be: "))
            if length <= 0:
                print("Enter a number greater than zero")
            else:
                return length
        except ValueError:
            print("Invalid Input Enter a Number")

def pass_quota(prompt):
    while True:
        answer = input(prompt).lower().strip()
        # print(answer)
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n": 
            return False
        else:
            print("Invalid input")
        
pass_length = length()
Upper = pass_quota("Should I Include Uppercase Letters: ")
Lower = pass_quota("Should I Include Lowercase Letters: ")
Nums = pass_quota("Should I Include Numbers: ")
Symb = pass_quota("Should I Include Symbols: ")


uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

characters = ""
if Upper:
    characters += uppercase
if Lower:
    characters += lowercase    
if Nums:
    characters += numbers
if Symb:
    characters += symbols
# print(characters)

if characters == "":
    print("You must select at least one character type.")
    exit()

password = ""

for i in range(pass_length):
    password += random.choice(characters)
    
print(password)    