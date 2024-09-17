import sys

# Braille Dictionary for letters (Lowercase)
braille_alphabet = {
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..',
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..',
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.',
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.', 
    's': '.OO.O.', 
    't': '.OOOO.',
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Capital follow symbol and numbers follow symbol
braille_capital = '.....O'
braille_number = '.O.OOO'

# Braille numbers 0-9 (braille_number is a prefix)
braille_numbers = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..',
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..'
}

#Dictionary for reverse case of converting braille to english
numbers_braille = {v: k for k, v in braille_numbers.items()}

#Dictionary for reverse case of converting braille to english
english_braille = {v: k for k, v in braille_alphabet.items()}

# Function to determine if input is Braille or English
def is_braille(input_string):
    return all(char in ['O', '.'] for char in input_string) #Returns true if all chars are a O or .

# Function to translate from English to Braille
def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_number)
                number_mode = True
            result.append(braille_numbers[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False  # Exit number mode when an alphabet is encountered
            if char.isupper():
                result.append(braille_capital)
            result.append(braille_alphabet[char.lower()])
        elif char == ' ':
            result.append('......')  # Space in Braille
            number_mode = False  # Reset number mode on space
    return ''.join(result)

# Function to translate from Braille to English
def braille_to_english(braille):
    result = []
    index = 0
    capital_mode = False
    number_mode = False
    while index < len(braille):
        symbol = braille[index:index + 6]
        
        if symbol == braille_capital:
            capital_mode = True
        elif symbol == braille_number:
            number_mode = True
        elif symbol == '......':  # Space in Braille
            result.append(' ')
            number_mode = False
        else:
            if number_mode:
                # Translate as number
                result.append(numbers_braille[symbol])

                while index < len(braille) - 6 and symbol != '......':
                    index += 6
                    symbol = braille[index:index + 6]
                    result.append(numbers_braille[symbol])
                    
                number_mode = False
            else:
                # Translate as letter
                if capital_mode:
                    result.append(english_braille[symbol].upper())
                    capital_mode = False
                else:
                    result.append(english_braille[symbol])
            # Reset number_mode after encountering a non-number
            number_mode = False  
        index += 6
    return ''.join(result)

# Main function to handle the translation logic
def main():
    input_string = sys.argv[1]
    
    if is_braille(input_string):
        # Input is Braille, translate to English
        translated_text = braille_to_english(input_string)
    else:
        # Input is English, translate to Braille
        translated_text = english_to_braille(input_string)
    
    # Output the translated string
    print(translated_text)

if __name__ == "__main__":
    main()
