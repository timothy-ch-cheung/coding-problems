import glob

from pathlib import Path

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


def read_file(fileName):
    with open(fileName) as file:
        Path("word_to_smorse/").mkdir(parents=True, exist_ok=True)
        Path("smorse_to_word/").mkdir(parents=True, exist_ok=True)
        count = 0
        for idx, word in enumerate(file):
            word = word.strip()
            word_length = len(word)
            smorsed_word = smorse(word)
            smorsed_word_length = len(smorsed_word)
            with open("smorse_to_word/" + str(smorsed_word_length) + "chars", "a+") as smorse_to_word_file:
                smorse_to_word_file.write(smorsed_word + "=" + word + "\n")
            with open("word_to_smorse/" + str(word_length) + "letters", "a+") as word_to_smorse_file:
                word_to_smorse_file.write(word + "=" + smorsed_word + "\n")
            if idx % 1000 == 0:
                print("processed {} thousand words".format(count))
                count += 1


def get_words_matching_smorse(smorse):
    smorsed_word_length = len(smorse)
    results = []
    with open("smorse_to_word/" + str(smorsed_word_length) + "chars", "a+") as smorse_to_word_file:
        for line in smorse_to_word_file:
            word_pair = line.split("=")
            if word_pair[0] == smorse:
                results.append(word_pair[1].strip())
    return results


def get_words_matching_smorse_predicate(fun, file=None):
    if not file:
        files_to_search = glob.glob("smorse_to_word/*")
    else:
        files_to_search = ["smorse_to_word/" + file]

    results = []
    for files in files_to_search:
        with open(files) as current_file:
            for line in current_file:
                word_pair = line.split("=")
                if fun(word_pair[0]):
                    results.append(word_pair[1].strip())
    return results


# Bonus 1 #
def get_one_smorse_matching_13_words():
    return ""


# Bonus 2 #
def contains_15_dashes(string):
    return "-" * 15 in string


def get_word_for_15_dash_smorse():
    fifteen_dash_word = get_words_matching_smorse_predicate(contains_15_dashes)[0]
    print(fifteen_dash_word)
    return smorse(fifteen_dash_word)


print(get_word_for_15_dash_smorse())


# Bonus 3 #
def get_21_letter_word_with_perfectly_balanced_smorse():
    return ""


# Bonus 4 #
def get_13_letter_word_that_is_smorse_palindrome():
    return ""


# Bonus 5 #
def get_four_13_character_non_occuring_smorse_sequences():
    return ""

# readFile("enable1.txt")
