print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

over_message = "Game Over"

cross_road = input("You are at a cross road. Where do you want to go? Type 'Left' or 'Right'").lower()

if cross_road == "left":
    lake = input("You came to a lake. There is an island middle of the lake. Type 'Wait' for a boat or type 'Swim' to swim across. ").lower()
    if lake == "wait":
        door = input("You arrived at the island unharmed. There is a house with three doors. one 'red', one 'yello', one 'blue'. Which coller do you choose? ").lower()
        if door == "yellow":
            print("You win!")
        elif door == "red":
            print(f"Burned by fire. {over_message}")
        elif door == "blue":
            print(f"Eaten by a Beast. {over_message}")
        else:
            print(over_message)
    else:
        print(f"Attack by a trout. {over_message}")
else:
    print(f"Fall into a hole. {over_message}")