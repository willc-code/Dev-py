# The Caesar Cipher!

About: Caesar probably wished he had this - A python CLI message encoder/decoder. 

## How to use 

Run `python main.py` and follow the prompts to input the relevant responses. 

## What it does

Helping you to encode or decode your secret messages according to your preference. 

## Other files

draft.py - This is the draft version where i figured out the main mechanics behind the shifting of index numbers before attempting the project.
caesar_cipher_art.py - contains the logo of the game in ASCII art, which is then imported to main.py
### Learning outcomes

- defining custom function with three parameters/inputs, and using it. 
- The Modulo Operator (%). This "wraps" the index back to the beginning if it exceeds 25. This is to overcome the common issue when you shift a letter near the end of the alphabet. If you try to shift 'z' by 1, your code looks for the index 26, but the list only goes up to 25. this will result in error. 
- practicing while loop - to keep the game going as long as the condition was not met, and breaking it when the guess is right.
