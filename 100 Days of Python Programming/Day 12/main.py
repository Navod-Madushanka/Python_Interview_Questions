import random
print("Welcome to the number guessing Game!")
print("I am thinking of a number between 1 - 100")

HARD_LEVEL = 5
EASY_LEVEL = 10

number = random.randint(1, 100);

def loop_function(loop):
    for n in range(loop):
        print(f"You have {loop-n} attempts")
        guess = int(input("Make a Guess: "))

        if guess > number:
            print("Too high.\nGuess again!")
        elif guess < number:
            print("Too low.\nGuess again!")
        else:
            print(f"You get it! answer was {number}")
            break

difficulty_level = input("Choose Difficulty level: Type 'easy' or 'hard' ").lower()

play_again = True

while play_again:
    if difficulty_level == "easy":
        loop_function(EASY_LEVEL)
    else:
        loop_function(HARD_LEVEL)
    if input("GO you want to play again? Type 'y' or 'n'").lower() == 'n':
        play_again = False