import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_item_Count = len(names)

payer_name = names[random.randint(0,list_item_Count - 1)]

print(f"{payer_name} is going to buy the meal today!")