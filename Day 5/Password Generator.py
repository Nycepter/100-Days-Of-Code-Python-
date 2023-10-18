import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_password_characters = []
random_password_characters_randomized = []
list_to_string = ""
for times in range(0, nr_letters):
    random_password_characters += random.choice(letters)
for times in range(0, nr_numbers):
    random_password_characters += random.choice(numbers)
for times in range(0, nr_symbols):
    random_password_characters += random.choice(symbols)
for times in range(len(random_password_characters)):
    char = random.choice(random_password_characters)
    random_password_characters_randomized.append(char)
    random_password_characters.remove(char)
random_password = list_to_string.join(random_password_characters_randomized)
print(f"Your password is: {random_password}")
