PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() #Get names from invited names
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contains = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contains.replace(PLACEHOLDER, stripped_name) # Replace [name] with invited names

        # Write the letters into new file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        