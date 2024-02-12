import random
import game_data
import art

print(art.logo)

SCORE = 0

def compare_data(itemA,itemB):
    print(f"Compare A: {itemA['name']}, {itemA['description']} from {itemA['country']}")
    print(art.vs)
    print(f"Compare B: {itemB['name']}, {itemB['description']} from {itemB['country']}")

    if itemA['follower_count'] < itemB['follower_count']:
        higher_followers = "B"
    else:
        higher_followers = "A"
    return higher_followers


play_again = True
while play_again:
    itemA = game_data.data[random.randint(0, len(game_data.data)) - 1]
    itemB = game_data.data[random.randint(0, len(game_data.data)) - 1]
    higher_followers = compare_data(itemA, itemB)
    if input("Who has more followers? A or B?: ").upper() == higher_followers:
        SCORE += 1
        print(f"You're Right! current score is: {SCORE}")
    else:
        print(f"Sorry, That's wrong. Final score is: {SCORE}")
        play_again = False