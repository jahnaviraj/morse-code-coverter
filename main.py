""" A TEXT BASED PYTHON PROGRAM TO CONVERT STRINGS INTO MORSE CODE"""
"""ALSO HAS DECRYPTION OF MORSE CODE"""

#Morse code dict 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


#Function to convert string into morse code 
def convert_to_morse(text):
    """Takes string arg and returns morse code for it."""
    morse_code = ''
    for letter in text:
        #Adds morse code with 1 space for each letter
        if letter != ' ':   
            try:
                morse_code += MORSE_CODE_DICT[letter] + ' '
            except KeyError:
                print(f"{letter} does not have a morse code. Enter a string without {letter}.")
                return convert_to_morse(input('Enter new string: ').upper())
        else:
            #Adds 2 spaces for a space in string
            morse_code += '  '
    #Returns final morse_code
    return morse_code


#Function to convert morse into text
def convert_to_text(morse_code):
    """Takes morse code arg and return text string of the code."""
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
    return string.capitalize().replace("  ", ' ')


#Take string input 
text_to_convert = input("Enter the text you want to covert to Morse Code: ").upper()

#Take morse input 
morse_to_covert = input("Enter morse code to convert to string: ")

