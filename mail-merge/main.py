#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as guests:
    for guest in guests.readlines():
        with open("./Input/Letters/starting_letter.txt") as template_letter:
            with open(f"./Output/ReadyToSend/letter_to_{guest.strip()}.txt", mode="a") as letter:
                letter.write(template_letter.read().replace(PLACEHOLDER, guest.strip()))