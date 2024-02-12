MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "pennie": 0.01
}


def check_resources(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        return f"Sorry the water level of our resources is not enough to make {coffee} "
    elif resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
        return f"Sorry the milk level of our resources is not enough to make {coffee} "
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        return f"Sorry the coffee level of our resources is not enough to make {coffee} "
    else:
        return True


def check_cost(coffee):
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))

    total = quarters + dimes + nickles + pennies

    if MENU[coffee]["cost"] <= total:
        balance = total - MENU[coffee]["cost"]
        print(f"Balance is ${balance}")
    else:
        return False


play_again = True
while play_again:
    coffee = input("    What would you like? (espresso/latte/cappuccino): ").lower()

    resources_msg = check_resources(coffee)
    cost_msg = check_cost(coffee)

    if not resources_msg:
        print(resources_msg)
        play_again = False
    elif cost_msg == False:
        print(f"You don't have enough money")
        play_again = False
    else:
        print("Enjoy your coffee")
