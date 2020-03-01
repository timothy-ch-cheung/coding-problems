from Smooshed_Morse_Code_1.smooshed_morse_code import smorse, get_word_for_15_dash_smorse, \
    get_perfectly_balanced_words_21_letter, get_13_letter_word_that_is_smorse_palindrome, get_words_matching_smorse, \
    get_four_13_character_non_occuring_smorse_sequences, get_one_smorse_matching_13_words


# Smorse Tests #

def test_smorse_should_return_sos():
    assert smorse("sos") == "...---..."


def test_smorse_should_return_daily():
    assert smorse("daily") == "-...-...-..-.--"


def test_smorse_should_return_programmer():
    assert smorse("programmer") == ".--..-.-----..-..-----..-."


def test_smorse_should_return_bits():
    assert smorse("bits") == "-.....-..."


def test_smorse_should_return_three():
    assert smorse("three") == "-.....-..."


def test_get_words_matching_smorse():
    assert get_words_matching_smorse(".-")[0].word == "et"


# BONUS 1 # Find the only sequence that's the code for 13 different words.
def test_bonus_1_should_return_13_different_words():
    word_pairs = set(get_one_smorse_matching_13_words())
    sequence = word_pairs[0].smorse
    assert len(word_pairs) == 13
    for wp in word_pairs:
        assert wp.smorse == sequence


# BONUS 2 # Find the word with 15 dashes in a row.
def test_bonus_2_should_return_smorse_with_15_dashes_in_row():
    word_pair = get_word_for_15_dash_smorse()
    assert ("-" * 15 in word_pair.smorse)
    print("\n", word_pair.smorse)


# BONUS 3 # Find the 21 letter word which has perfectly balanced smorse (that is not counterdemonstrations).
def test_bonus_3_should_return_perfectly_balanced_21_letter_word():
    word_pair = get_perfectly_balanced_words_21_letter()
    sequence = smorse(word_pair.word)
    assert sequence.count(".") == sequence.count("-")
    assert len(word_pair.word) == 21
    assert word_pair.word != "counterdemonstrations"
    assert sequence == word_pair.smorse
    print("\n", word_pair.word, "=", sequence)


# BONUS 4 #  Find the only 13-letter word that encodes to a palindrome
def test_bonus_4_should_return_13_letter_smorse_palindrome():
    word_pair = get_13_letter_word_that_is_smorse_palindrome()
    assert len(word_pair.word) == 13
    assert word_pair.smorse == word_pair.smorse[::-1]


# BONUS 5 #  --.---.---.-- is one of five 13-character sequences that does not appear in the encoding of any word.
# Find the other four.
def test_bonus_5_should_return_4_non_occuring_sequences():
    sequences = get_four_13_character_non_occuring_smorse_sequences()
    sequences = [x != "--.---.---.--" for x in sequences]
    assert len(sequences) == 4
    for seq in sequences:
        assert len(get_words_matching_smorse(seq)) == 0
