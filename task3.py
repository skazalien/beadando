MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

def encrypt(message): #msg to morse
    inmorse = ''
    for i in message:
        if i != ' ':
            inmorse += MORSE_CODE_DICT[i] + ' '
        else:
            inmorse += '\t'

    return inmorse

def decrypt(message): #morse to msg
    message += ' '      #ha nem lenne a végén egy ' ', akkor hozzátesz, amúgy kihagyná az utolsó betűt
    regular = ''
    tarol = ''
    for j in message.replace('\t', ' '): # j = letter
        if j != ' ':
            space_in_between = 0
            tarol += j                 #morse kód tárolása egy betűvel
        else:
            space_in_between += 1
            if space_in_between == 2:
                regular += ' '
            else:                       # a kulcsok elérése a value-k segítségével
                regular += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(tarol)]
                tarol = ''

    return regular

message = input("Message: ").strip() # < > = {} []
dotordash = [".","-"]

if message[0].upper() in list(MORSE_CODE_DICT.keys()) and message[0] not in dotordash:
    result_in_morse = encrypt(message.upper())
    print("Original Message in Morse:", result_in_morse)
    print("Original Message:", message)
else:
    result_in_regular = decrypt(message)
    result_in_regular=result_in_regular.capitalize()
    print("Original Message in Regular:", result_in_regular)
    print("Original Message:", message)
