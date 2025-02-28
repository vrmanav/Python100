alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encode(user_input, shift_number):
    encoded_text = ""
    for current_letter in user_input:
        old_index = alphabet.index(current_letter)
        new_index = (old_index + shift_number) % 26
        encoded_text += alphabet[new_index]
    print(f"\n{encoded_text}")


def decode(user_input, shift_number):
    decoded_text = ""
    for current_letter in user_input:
        old_index = alphabet.index(current_letter)
        new_index = (old_index - shift_number) % 26
        decoded_text += alphabet[new_index]
    print(f"\n{decoded_text}")


user_input = input("Enter your passphrase:\n")
operation = input("Do you want to encode or decode it [ENCODE/DECODE]:\n").lower()
shift_number = int(input("Type shift number:\n"))

if user_input == "encode":
    encode(user_input, shift_number)
elif user_input == "decode":
    decode(user_input, shift_number)
