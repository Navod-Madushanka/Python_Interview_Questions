PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()


with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_Content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_Content.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)

