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

data = pandas.read_csv(
    "C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 25/weather_data.csv")

print(data["temp"])
