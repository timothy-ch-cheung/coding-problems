import glob
from enum import Enum

from pathlib import Path


class WordPair():
    def __init__(self, word, smorse):
        self.word = word
        self.smorse = smorse


class Type(Enum):
    SMORSE = "smorse_to_word"
    WORD = "word_to_smorse"


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


def read_file(file_name):
    with open(file_name) as file:
        Path(Type.WORD + "/").mkdir(parents=True, exist_ok=True)
        Path(Type.SMORSE + "/").mkdir(parents=True, exist_ok=True)
        count = 0
        for idx, word in enumerate(file):
            word = word.strip()
            word_length = len(word)
            smorsed_word = smorse(word)
            smorsed_word_length = len(smorsed_word)
            with open(Type.SMORSE + "/" + str(smorsed_word_length) + "chars", "a+") as smorse_to_word_file:
                smorse_to_word_file.write(word + "=" + smorsed_word + "\n")
            with open(Type.WORD + "/" + str(word_length) + "letters", "a+") as word_to_smorse_file:
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


def get_words_matching_smorse_predicate(fun, directory=None, file=None, string_type=None):
    if not string_type or not directory:
        return
    if not file:
        files_to_search = glob.glob(directory + "/*")
    else:
        files_to_search = [directory + "/" + file]

    results = []
    for files in files_to_search:
        with open(files) as current_file:
            for line in current_file:
                pair = line.strip().split("=")
                word_pair = WordPair(pair[0], pair[1])
                word_to_check = word_pair.word if string_type == Type.WORD else word_pair.smorse
                if fun(word_to_check):
                    results.append(word_pair)
    return results


# Bonus 1 #
def get_one_smorse_matching_13_words():
    return ""


# Bonus 2 #
def contains_15_dashes(string):
    return "-" * 15 in string


def get_word_for_15_dash_smorse():
    fifteen_dash_word = \
    get_words_matching_smorse_predicate(contains_15_dashes, directory=Type.SMORSE.value, string_type=Type.SMORSE)[0]
    return smorse(fifteen_dash_word.word)


# print(get_word_for_15_dash_smorse())


# Bonus 3 #
def is_perfectly_balanced(string):
    return string.count(".") == string.count("-")


def get_perfectly_balanced_words_21_letter():
    results = get_words_matching_smorse_predicate(is_perfectly_balanced, directory=Type.WORD.value, file="21letters",
                                                  string_type=Type.SMORSE)
    result = next(filter(lambda x: x.word != "counterdemonstrations", results))
    return result.word


# Bonus 3 #
def get_21_letter_word_with_perfectly_balanced_smorse():
    return ""


# Bonus 4 #
def get_13_letter_word_that_is_smorse_palindrome():
    return ""


# Bonus 5 #
def get_four_13_character_non_occuring_smorse_sequences():
    return ""

# read_file("enable1.txt")
