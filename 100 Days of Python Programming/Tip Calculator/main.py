print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_val = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = float(input("How many people to split the bill? "))

percentage = bill / 100 * percentage_val

total = round((bill + percentage) / people_count, 2)
print(f"Each person should pay: {total}")

