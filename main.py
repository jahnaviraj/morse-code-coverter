""" A TEXT BASED PYTHON PROGRAM TO CONVERT STRINGS INTO MORSE CODE"""
"""ALSO HAS DECRYPTION OF MORSE CODE"""

import argparse

#Morse code dict 
from data import MORSE_CODE_DICT

def parse_args():
    parser = argparse.ArgumentParser(description='Convert to morse code')
    parser.add_argument('-t','--text', type=str, help='String to convert to morse', default=None)
    parser.add_argument('-c','--code', type=str, help='Morse code to convert to string', default=None)
    parser.add_argument('-m','--method', type=str, choices=['t2m', 'm2t'])
    args = parser.parse_args()
    if args.method== 't2m' and args.text:
        convert_to_morse(args.text)
    elif args.method == 'm2t' and args.code:
        convert_to_text(args.code)
        
#Function to convert string into morse code 
def convert_to_morse(text):
    """Takes string arg and prints morse code for it."""

    morse_code = ''
    for letter in text.upper():
        #Adds morse code with 1 space for each letter
        if letter != ' ':   
            try:
                morse_code += MORSE_CODE_DICT[letter] + ' '
            except KeyError:
                print(f"{letter} does not have a morse code. Enter a string without {letter}.")
                return convert_to_morse(input(f"Enter new text without {letter}: "))
        else:
            #Adds 2 spaces for a space in string
            morse_code += '  '
    #Returns final morse_code
    print(f"The morse code for '{text}' is '{morse_code}'")

#Function to convert morse into text
def convert_to_text(morse_code):
    """Takes morse code arg and prints text string of the code."""

    #Makes a dict for the morse codes
    morse_dict = morse_code.split(' ')
    string = ''
    #Loop through each code in string
    for input_code in morse_dict:
        #Adds space for each space in code 
        if input_code == '':
            string += ' '
        else:
            #Searches the dict for the letter for the code and adds to string 
            for letter, morse in MORSE_CODE_DICT.items():
                if morse == input_code:
                    string += letter
    #Return the final string, since 2 spaces are used in morse to seperate words, replace double space with single space.
    final_string = string.capitalize().replace("  ", ' ')
    print(f"The text for '{morse_code}' is '{final_string}'")

if __name__ == "__main__":
    parse_args()   

