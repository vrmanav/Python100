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

# def encode(original_text, shift_number):
#     encoded_text = ""
#     for current_letter in original_text:
#         old_index = alphabet.index(current_letter)
#         new_index = (old_index + shift_number) % 26
#         encoded_text += alphabet[new_index]
#     print(f"\nEncoded text: {encoded_text}")

# def decode(original_text, shift_number):
#     decoded_text = ""
#     for current_letter in original_text:
#         old_index = alphabet.index(current_letter)
#         new_index = (old_index - shift_number) % 26
#         decoded_text += alphabet[new_index]
#     print(f"\nDecoded text: {decoded_text}")


def caesar_cipher(original_text, operation, shift_number):
    output_text = ""
    if operation == "decode":
        shift_number *= -1
    for current_letter in original_text:
        if current_letter not in alphabet:
            output_text += current_letter
        else:
            old_index = alphabet.index(current_letter)
            new_index = (old_index + shift_number) % 26
            output_text += alphabet[new_index]
    print(f"\n{operation.capitalize()}d text is: {output_text}")


original_text = input("Enter your passphrase:\n")
operation = input("Do you want to encode or decode it [ENCODE/DECODE]:\n").lower()
shift_number = int(input("Type shift number:\n"))
caesar_cipher(original_text, operation, shift_number)

# if operation == "encode":
#     encode(user_input, shift_number)
# elif operation == "decode":
#     decode(user_input, shift_number)
