import random

print("This is a password generator, just answer a few questions and we'll create a custom password for you.")

adding_letters = []
string = ""

def take_letters_out(x):
    for t in x:
        adding_letters.append(t)

try:
    name = take_letters_out(input("What's your name?: "))
    age = take_letters_out(input("Whats your age?: "))
    color = take_letters_out(input("What's your favorite color?: "))
except ValueError:
    print("Invalid input, try again please.")
    
random.shuffle(adding_letters)

for y in adding_letters:
    string = string + y

print(string)