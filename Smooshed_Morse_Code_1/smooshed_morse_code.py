MORSE = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- " \
        "--.. ".split(" ")
LOWER_CASE_OFFSET = 97

MORSE_CODE = {chr(i + LOWER_CASE_OFFSET): MORSE[i] for i in range(0, len(MORSE))}
print(MORSE_CODE)

def smorse(word):
    smorse_code = ""
    for letter in word:
        smorse_code += MORSE_CODE[letter]
    return smorse_code
