from Smooshed_Morse_Code_1.smooshed_morse_code import smorse, get_words_matching_smorse, \
    get_word_for_15_dash_smorse


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
