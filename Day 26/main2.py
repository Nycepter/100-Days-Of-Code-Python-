
# names = ["Aelx", "Alexander", "Aaron", "Maranda", "Nycepter", "Pip"]

# names2 = [name.upper() for name in names if len(name) > 5]

# # print(names2)

# squared_numbers = [number * number for number in numbers]

# numbers = [int(number) for item in list_of_strings]

# even_num = [number for number in numbers if number % 2 == 0]


with open("100-Days-Of-Code-Python-/Day 26/file1.txt", mode="r") as file1:
    list1 = file1.readlines()

with open("100-Days-Of-Code-Python-/Day 26/file2.txt", mode="r") as file2:
    list2 = file2.readlines()

both_lists = [int(number) for number in list1 if number in list2]

print(both_lists)
