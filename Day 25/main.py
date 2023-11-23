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


temp_list = data["temp"].to_list()
temp_total = 0
for temp in temp_list:
    temp_total += temp

avg = round(temp_total / len(temp_list), 1)


print(data[data.temp == data["temp"].max()])
