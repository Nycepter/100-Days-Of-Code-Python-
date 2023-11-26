import csv
import pandas


# with open("C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 25/weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()


# with open("C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 25/weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# data = pandas.read_csv(
#     "C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 25/weather_data.csv")


# temp_list = data["temp"].to_list()
# temp_total = 0
# for temp in temp_list:
#     temp_total += temp

# avg = round(temp_total / len(temp_list), 1)


# print(data[data.temp == data["temp"].max()])


data = pandas.read_csv(
    "C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231124.csv")
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# for color in data["Primary Fur Color"]:
#     if color == "Gray":
#         gray += 1
#     elif color == "Black":
#         black += 1
#     else:
#         red += 1

print(red_squirrels)
print(black_squirrels)
print(gray_squirrels)


data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

Squirrel_data = pandas.DataFrame(data_dictionary)
Squirrel_data.to_csv(
    "C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 25/Squirrel Data.csv")
