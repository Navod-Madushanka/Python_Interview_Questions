import random
import Stages

print('''
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
''')

word_list = ['apple', 'banana', 'car', 'dog', 'elephant', 'frog', 'guitar', 'house', 'ice cream', 'jacket', 'kangaroo', 'lion', 'mountain', 'noodle', 'ocean', 'pencil', 'queen', 'river', 'sun', 'tree', 'umbrella', 'violin', 'waterfall', 'xylophone', 'yacht', 'zebra', 'airplane', 'beach', 'camera', 'desk', 'ear', 'flower', 'globe', 'hat', 'island', 'jellyfish', 'key', 'lighthouse', 'moon', 'notebook', 'orange', 'penguin', 'quilt', 'rain', 'sunglasses', 'train', 'umbrella', 'volcano', 'watermelon', 'xylophone', 'yogurt', 'zeppelin', 'bicycle', 'book', 'cookie', 'door', 'elephant', 'fireplace', 'garden', 'hamburger', 'igloo', 'jungle', 'koala', 'lamp', 'mailbox', 'night', 'octopus', 'painting', 'quilt', 'road', 'snake', 'telephone', 'universe', 'violin', 'water', 'xylophone', 'yarn', 'zoo', 'alarm', 'basketball', 'clock', 'dolphin', 'earring', 'fire', 'giraffe', 'helicopter', 'ice', 'jacket', 'kite', 'laptop', 'mushroom', 'necklace', 'owl', 'pizza', 'queen', 'robot', 'sandwich', 'turtle', 'umbrella', 'volleyball', 'window', 'xylophone', 'yoga', 'zebra']
chosen_word = random.choice(word_list)

display = []
live = 0
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

while "_" in display:
    guess = input("Guess a letter?").lower()

    hangman = display
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess in display:
        print("You already Guess that letter!")

    if guess not in chosen_word:
        print("You guess a wrong letter. I Have to take one life!")
        print(Stages.hangman_art[live])
        live += 1

    if live == 7:
        print("You Lose")
        print(f"The word is {chosen_word}")
        break;
    print(display)

if "_" not in display:
    print("You Win")
