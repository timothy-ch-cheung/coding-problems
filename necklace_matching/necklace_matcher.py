from pathlib import Path

from necklace_matching.necklace import Necklace


def same_necklace(string_a, string_b):
    necklace_a = Necklace(string_a)
    necklace_b = Necklace(string_b)
    return necklace_a == necklace_b


def repeats(string):
    if not string:
        return 1
    count = 0
    repeated = string + string
    for i in range(len(string)):
        temp = repeated[i:i + len(string)]
        if string == temp:
            count += 1
    return count


def get_4_words_same_necklace():
    with open(str(Path.cwd().parent) + "/enable1.txt") as file:
        words_by_length = {}
        for word in file:
            word = word.strip()
            if len(word) in words_by_length:
                words_by_length[len(word)].append(word)
            else:
                words_by_length[len(word)] = [word]
    for current_list in words_by_length.values():
        necklaces = {}
        for current_word in current_list:
            hashed = Necklace(current_word)
            if hashed in necklaces:
                necklaces[hashed].append(current_word)
            else:
                necklaces[hashed] = [current_word]
            if len(necklaces[hashed]) == 4:
                return necklaces[hashed]
