# Dictionaries for Morse Code to English and Vise-versa
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


# English to Morse Code
def mc_convert(text):
    words = ''
    for letter in text.upper():
        if letter != ' ':
            words += MORSE_CODE_DICT.get(letter, '') + ' '
        else:
            words += '/ '
    return words.strip()


# Morse Code to English
def eng_convert(text):
    text += ' '
    decipher = ''
    citext = ''
    for letters in text:
        if letters != ' ' and letters != '/':
            citext += letters
        else:
            if citext:
                decipher += REVERSE_MORSE_CODE_DICT.get(citext, '')
                citext = ''
            if letters == '/':
                decipher += ' '
    return decipher.strip()


# Function to check if message is Morse Code or English
def check_message(text):
    if any(char in ['.', '-'] for char in text) and (' ' in text or '/' in text):
        return eng_convert(text)
    else:
        return mc_convert(text)


message = input('Enter message:')
result = check_message(message)

print(f"Original : {message}\nConverted: {result}\n")
