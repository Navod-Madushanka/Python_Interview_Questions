import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
computer = []
user = []

def chose_card(card_to):
    if card_to == "both":
        computer.append(random.choice(cards))
        user.append(random.choice(cards))
    elif card_to == "computer":
        computer.append(random.choice(cards))
    else:
        user.append(random.choice(cards))

def rules():
    winner = ""
    sum_of_computer = sum(computer)
    sum_of_user = sum(user)

    if sum_of_computer == 21 or sum_of_user == 21:
        if sum_of_computer == sum_of_user:
            print("Draw")
        #     Play Again
        elif sum_of_computer == 21:
            winner = "Computer"
            play_again = False
        else:
            winner = "User"
            play_again = False
    elif sum_of_computer > 21 or sum_of_user > 21:
        if sum_of_computer > 21:
            if computer[0] == 11:
                computer[0] = 1
            elif computer[1] == 11:
                computer[1] = 1

            if sum(computer) == 21:
                winner = "Computer"
            else:
                winner = "User"
            play_again = False
        else:
            if user[0] == 11:
                user[0] == 1
            elif user[1] == 11:
                user[1] = 1;

            if sum(user) == 21:
                winner = "User"
            else:
                winner = "Computer"
            play_again = False
    else:
        draw_card = input("DO you want to draw a card? yes 'y' or no 'n'").lower()
        return draw_card
    return winner

play_again = True
while play_again:
    if len(computer) == 2 and len(user) == 2:
        print(f"Your cards are {user}")
        print(f"computers first card is {computer[0]}")
        output_in_rules = rules()
        if output_in_rules == "User":
            print(f"User Win")
            play_again = False
        elif output_in_rules == "Computer":
            print("Computer wins")
            play_again = False
        else:
            if output_in_rules == "y":
                computer[0] = sum(computer)
                computer.pop(1)
                user[0] = sum(user)
                user.pop(1)
                play_again = True
            else:
                if sum(computer) > sum(user):
                    print("Computer Win")
                    play_again = False
                elif sum(computer) < sum(user):
                    print("User Win")
                    play_again = False

    else:
        chose_card("both")
