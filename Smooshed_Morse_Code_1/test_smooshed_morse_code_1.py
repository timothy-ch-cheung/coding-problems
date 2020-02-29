from Smooshed_Morse_Code_1.smooshed_morse_code import smorse, get_word_for_15_dash_smorse, get_perfectly_balanced_words_21_letter


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


# BONUS 1 # Find the only sequence that's the code for 13 different words.
# def test_bonus_1_should_return_13_different_words():
#     sequence = get_smorse_for_13_words()
#     assert len(set(get_words_matching_smorse(sequence))) == 13

# BONUS 2 # Find the word with 15 dashes in a row.
def test_bonus_2_should_return_smorse_with_15_dashes_in_row():
    sequence = get_word_for_15_dash_smorse()
    assert ("-" * 15 in sequence) == True
    print("\n",sequence)


# BONUS 3 # Find the 21 letter word which has perfectly balanced smorse (that is not counterdemonstrations).
def test_bonus_3_should_return_perfectly_balanced_21_letter_word():
    word = get_perfectly_balanced_words_21_letter()
    sequence = smorse(word)
    assert sequence.count(".") == sequence.count("-")
    assert len(word) == 21
    assert word != "counterdemonstrations"
    print("\n",word, "=", sequence)
