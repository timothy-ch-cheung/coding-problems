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
    return []
