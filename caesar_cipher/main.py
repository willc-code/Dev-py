from caesar_cipher_art import logo

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# while loop and variable equals to False to keep the game going as long as the user say yes.
game_over = False

while game_over == False:

    # getting user to input the relevant information especially their message
    crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    message = input("Type your message: \n").lower()
    shift_number = int(input("Type your shift number: \n"))

    # defining the encrypt function. Encrypt is for the user to choose to encode or decode.
    def encrypt(crypt, message, shift_number):
        if crypt == "encode":
            shifted_message = ""

            # shift index is the index number of the letter in the message plus or minus (depending on encode or decode) the shift number.
            # the shift index is then added to the the variable 'shifted_message', which will be printed out as the outcome.
            for letter in message:
                shift_index = (int(alphabet.index(letter)) + shift_number) % 26
                shifted_message += str(alphabet[shift_index])

            print(f"Here is the encoded result: {shifted_message}")



        elif crypt == "decode":
            shifted_message = ""

            for letter in message:
                shift_index = (int(alphabet.index(letter)) - shift_number) % 26
                shifted_message += str(alphabet[shift_index])

            print(f"Here is the decoded result: {shifted_message}")



        else:
            print("Please type 'encode' or 'decode'")

    # this is where the function encrypt is being run, as part of the while loop.
    encrypt(crypt, message, shift_number)

    # this is where ws ask the user whether to continue or not.
    # If yes, the 'game_over' variable remains to be False, which keeps the game going.
    # Otherwise, it will be True which breaks the while loop.
    continue_game = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")
    if continue_game == "yes":
        game_over = False
    elif continue_game == "no":
        game_over = True
    else:
        print("Please type 'yes' or 'no'")

