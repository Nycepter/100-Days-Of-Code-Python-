dictionary = {
    'Aaron': "A cool guy",
    'Its fun to': "try new things",
}

dictionary['bingo'] = "bango"
dictionary['Libr'] = {
    'atom': "bomb",
    'nitrous': "oxide",
}
dictionary['list'] = ["thingy", "mabobber",]

dictionary['Libr']['add'] = "this thing"


class Aaron:
    age = 30
    weight = 195
    sport = "tennis"


class Robbie:
    age = 29
    weight = 150
    sport = "baseball"


dictionary2 = {
    'Aaron': Aaron,
    'Robbie': Robbie,
}


# for keys in dictionary:
#     print(keys)
#     print(dictionary[keys])

#     if dictionary[keys] == dictionary['Libr']:
#         for thing in dictionary['Libr']:
#             print(thing)
#             print(dictionary['Libr'][thing])

print(dictionary2)
