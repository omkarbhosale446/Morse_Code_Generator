english_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

morse_english_dict = {}
for key, value in english_morse_dict.items():
    morse_english_dict[value] = key


def english_to_morse(msg):
    morse = []
    for char in msg:
        if char in english_morse_dict:
            morse.append(english_morse_dict[char])
    return " ".join(morse)

def morse_to_englsh(msg):
    msg = msg.split(" ")
    english = []
    for code in msg:
        if code in morse_english_dict:
            english.append(morse_english_dict[code])
    return " ".join(english)


def convert(direction):
    if direction == "1":
        encrypt = english_to_morse(msg=message)
        print(encrypt)

    if direction == "2":
        decrypt = morse_to_englsh(msg=message)
        print(decrypt)

should_end = False

while not should_end:

    direction = input("Please choose '1' to convert English text to Morse code or "
                      "choose '2' to convert Morse code to English text. \n")

    if direction == "1":
        text = "English text to convert:"

    elif direction == "2":
        text = "Morse code to convert with space after each letter:"

    else:
        text = "Valid input of either '1' or '2'"

    message = input(f"Please provide {text} \n").lower()

    convert(direction=direction)

    restart = input("Would you like to run again? Enter 'y' for yes and 'n' for no. \n").lower()

    if restart == "n":
        should_end = True
        print("See you again!")



