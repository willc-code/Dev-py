# This is the draft version where i figured out the main mechanics behind the shifting of index numbers before attempting the project.

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

if crypt == "encode":
    message = input("Type your message: ").lower()
    shift_number = int(input("Type your shift number: "))
    shifted_message = ""

    for letter in message:
        shift_index = (int(alphabet.index(letter)) + shift_number) % 26
        shifted_message += str(alphabet[shift_index])

    print(shifted_message)

elif crypt == "decode":
    message = input("Type your message: ").lower()
    shift_number = int(input("Type your shift number: "))
    shifted_message = ""

    for letter in message:
        shift_index = (int(alphabet.index(letter)) - shift_number) % 26
        shifted_message += str(alphabet[shift_index])

    print(shifted_message)


