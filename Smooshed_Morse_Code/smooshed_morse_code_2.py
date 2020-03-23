from Smooshed_Morse_Code.smooshed_morse_code_1 import MORSE, LOWER_CASE_OFFSET

MORSE_CODE = {chr(i + LOWER_CASE_OFFSET): MORSE[i] for i in range(0, len(MORSE))}
MORSE_CODE_INVERSE = {MORSE[i]: chr(i + LOWER_CASE_OFFSET) for i in range(0, len(MORSE))}


def smalpha_helper(smorse_string, alphabet, alphabet_left):
    if len(smorse_string) == 0:
        return alphabet
    for letter in alphabet_left:
        morse = MORSE_CODE[letter]
        if smorse_string.startswith(morse):
            result = smalpha_helper(smorse_string[len(morse):], alphabet + MORSE_CODE_INVERSE[morse],
                                    alphabet_left.replace(letter, ""))
            if result is not None:
                return result
    return None


def smalpha(smorse_string):
    return smalpha_helper(smorse_string, "", "abcdefghijklmnopqrstuvwxyz")
