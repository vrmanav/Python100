formatted_invitees = []


def format_names():
    with open("Input/Names/invited_names.txt", mode="r") as names:
        invitees = names.readlines()
        for name in invitees:
            formatted_name = name.strip("\n")
            formatted_invitees.append(formatted_name)


def replace_placeholder():
    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        letter_as_str = starting_letter.read()
        
        # Replace [name] with the name of the invitee & create a new file
        for name in formatted_invitees:
            with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
                new_letter.write(letter_as_str.replace("[name]", f"{name}"))


format_names()
replace_placeholder()
