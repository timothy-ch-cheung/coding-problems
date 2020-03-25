import glob
from enum import Enum

from pathlib import Path

MORSE = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- " \
        "--..".split(" ")
LOWER_CASE_OFFSET = 97
SYMBOLS = {'.', '-'}

MORSE_CODE = {chr(i + LOWER_CASE_OFFSET): MORSE[i] for i in range(0, len(MORSE))}
print(MORSE_CODE)


class WordPair():
    def __init__(self, word, smorse):
        self.word = word
        self.smorse = smorse

    def __eq__(self, other):
        if not isinstance(other, WordPair):
            return NotImplemented
        return self.word == other.word and self.smorse == other.word


class Type(Enum):
    SMORSE = "smorse_to_word"
    WORD = "word_to_smorse"


class Trie():
    def __init__(self, char):
        self.char = char
        self.words = []
        self.next_chars = []

    def insert(self, string, word):
        length = len(string)
        if length == 0:
            self.words.append(word)
            return
        for char in self.next_chars:
            if string[0] == char.char:
                return char.insert(string[1:], word)
        self.next_chars.append(Trie(string[0]))
        return self.next_chars[-1].insert(string[1:], word)

    def __eq__(self, other):
        if not isinstance(other, Trie):
            return NotImplemented
        if self.char != other.char or self.words != other.words:
            return False
        for self_next, other_next in zip(self.next_chars, other.next_chars):
            if self_next != other_next:
                return False
        return True


def smorse(word):
    smorse_code = ""
    for letter in word:
        smorse_code += MORSE_CODE[letter]
    return smorse_code


def read_file(file_name):
    with open(file_name) as file:
        Path(Type.WORD.value + "/").mkdir(parents=True, exist_ok=True)
        Path(Type.SMORSE.value + "/").mkdir(parents=True, exist_ok=True)
        count = 0
        for idx, word in enumerate(file):
            word = word.strip()
            word_length = len(word)
            smorsed_word = smorse(word)
            smorsed_word_length = len(smorsed_word)
            with open(Type.SMORSE.value + "/" + str(smorsed_word_length) + "chars", "a+") as smorse_to_word_file:
                smorse_to_word_file.write(word + "=" + smorsed_word + "\n")
            with open(Type.WORD.value + "/" + str(word_length) + "letters", "a+") as word_to_smorse_file:
                word_to_smorse_file.write(word + "=" + smorsed_word + "\n")
            if idx % 1000 == 0:
                print("processed {} thousand words".format(count))
                count += 1


def get_word_pairs_matching_predicate(fun, directory=None, file=None, string_type=None):
    if not string_type or not directory:
        return []
    if not file:
        files_to_search = glob.glob(directory + "/*")
    else:
        path = Path(directory + "/" + file)
        if path.exists():
            files_to_search = [directory + "/" + file]
        else:
            return []

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


def get_words_matching_smorse(smorse):
    return get_word_pairs_matching_predicate(lambda x: x == smorse, directory=Type.SMORSE.value,
                                             string_type=Type.SMORSE)


# Bonus 1 #

def build_smorse_trie(words):
    trie = Trie("")
    for word_pair in words:
        trie.insert(word_pair.smorse, word_pair.word)
    return trie


TRIE = build_smorse_trie(get_word_pairs_matching_predicate(lambda x: True, directory=Type.SMORSE.value,
                                                           string_type=Type.SMORSE))


def traverse_helper(trie, fun, smorse):
    results = []
    for char in trie.next_chars:
        results += traverse_helper(char, fun, smorse + char.char)
    if fun(trie):
        results.append((trie.words, smorse))
    return results


def traverse(trie, fun):
    return traverse_helper(trie, fun, "")


def get_one_smorse_matching_13_words():
    results = traverse(TRIE, lambda x: len(x.words) == 13)
    print(results)
    return results[0]


# Bonus 2 #
def contains_15_dashes(string):
    return "-" * 15 in string


def get_word_for_15_dash_smorse():
    fifteen_dash_words = \
        get_word_pairs_matching_predicate(contains_15_dashes, directory=Type.SMORSE.value, string_type=Type.SMORSE)
    return fifteen_dash_words[0]


# Bonus 3 #
def is_perfectly_balanced(string):
    return string.count(".") == string.count("-")


def get_perfectly_balanced_words_21_letter():
    results = get_word_pairs_matching_predicate(is_perfectly_balanced, directory=Type.WORD.value, file="21letters",
                                                string_type=Type.SMORSE)
    result = next(filter(lambda x: x.word != "counterdemonstrations", results))
    return result


# Bonus 4 #
def is_palindrome(string):
    return string == string[::-1]


def get_13_letter_word_that_is_smorse_palindrome():
    return get_word_pairs_matching_predicate(is_palindrome, directory=Type.WORD.value, file="13letters",
                                             string_type=Type.SMORSE)[0]


# Bonus 5 #
def get_permutations_helper(length, string):
    results = []
    if (length == 0):
        return [string]
    for symbol in SYMBOLS:
        results += get_permutations_helper(length - 1, string + symbol)
    return results


def get_permutations(length):
    return get_permutations_helper(length, "")


def get_four_13_character_non_occuring_smorse_sequences():
    results = []
    permutations = get_permutations(13)
    for p in permutations:
        non_occuring = True
        for i in range(13, 79):
            file = "smorse_to_word/" + str(i) + "chars"
            path = Path(file)
            if path.exists():
                with open(file) as current_file:
                    for line in current_file:
                        pair = line.strip().split("=")
                        word_pair = WordPair(pair[0], pair[1])
                        if p in word_pair.smorse:
                            non_occuring = False
                            break
            if non_occuring is False:
                break
        if non_occuring:
            if len(results) == 4:
                return results
            results.append(p)
    return results


# Unused functions
def generate_remaining(prefix, length):
    results = []
    if length == 0:
        return [prefix]
    for symbol in SYMBOLS:
        results += generate_remaining(prefix + symbol, length - 1)
    return results


def get_non_ocurring_helper(trie, current_depth, string):
    next_symbols = set([x.char for x in trie.next_chars])
    missing_symbols = SYMBOLS - next_symbols
    results = []
    if current_depth == 0:
        return []
    for symbol in missing_symbols:
        results += generate_remaining(string + symbol, current_depth - 1)
    for symbol in trie.next_chars:
        results += get_non_ocurring_helper(symbol, current_depth - 1, string + symbol.char)
    return results


def get_non_ocurring(trie, target_depth):
    return get_non_ocurring_helper(trie, target_depth, "")

# read_file(str(Path.cwd().parent) + "/enable1.txt")
