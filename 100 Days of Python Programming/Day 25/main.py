import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp = data["temp"].tolist()
#
# print(data["temp"].max())
#
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp*9/5)+32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel count.csv")

