import re

logo = '''  _____      _             _____             
 / ____|    (_)           / ____|            
| |     _ __ _ _ __  ___| (___   __ _ _ __  
| |    | '__| | '_ \/ __|\___ \ / _` | '_ \ 
| |____| |  | | |_) \__ \____) | (_| | |_) |
 \_____|_|  |_| .__/|___/_____/ \__,_| .__/ 
               | |                    | |    
               |_|                    |_|    
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt\n")
text = input("Type your message:\n").lower()
shift = int(input("Type shift number:\n"))

def caesor(user_direction, plain_text, shit_amount):
    message = ""
    if user_direction == "encode":
        shit_amount = int(0 + shit_amount)
        message = "encoded Text"
    else:
        shit_amount = int(0 - shit_amount)
        message = "decoded Text"

    code = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter) + (shit_amount)
            code += alphabet[position]
    print(f"Your {message} is {code}")
    play_Again = input("Do you want to continue? type 'yes' or 'no'").lower()
    if play_Again == "yes":
        play = True
    else:
        print("Good Bye")
        play = False


def validations(text, shift):
    pattern = r'[0-9!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]'
    if re.search(pattern, text):
            print("You can only use Letters")
    elif shift > 26:
            print("Shift size is to high!")
        else:
            caesor(direction, text, shift)

validations(text,shift)