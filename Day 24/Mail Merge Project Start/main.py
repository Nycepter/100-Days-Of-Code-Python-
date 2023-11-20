
with open("C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

with open("C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 24/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    name = name.strip()
    updated_letter = letter.replace("[name]", name)
    with open(f"C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 24/Mail Merge Project Start/Output/ReadyToSend/Letter_to_{name}.txt", mode="w") as file:
        file.write(updated_letter)
