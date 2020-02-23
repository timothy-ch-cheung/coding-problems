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
        files_to_search = glob.glob("smorse_to_word/*.txt")
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
def get_smorse_for_13_words():
    return ""

# Bonus 2 #

# Bonus 2 #

# readFile("enable1.txt")
