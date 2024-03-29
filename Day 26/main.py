import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

phonetic_codes = pandas.read_csv(
    "100-Days-Of-Code-Python-/Day 26/nato_phonetic_alphabet.csv")
phonetic_codes_dict = phonetic_codes.to_dict()
df = pandas.DataFrame(phonetic_codes_dict)


letterdict = {row.letter: row.code for (index, row) in df.iterrows()}


word = input("Enter a word: ").upper()

output = [letterdict[letter] for letter in word]

print(output)
