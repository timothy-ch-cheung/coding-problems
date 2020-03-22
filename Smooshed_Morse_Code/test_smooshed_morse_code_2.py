import pytest

from Smooshed_Morse_Code.smooshed_morse_code_1 import smorse
from Smooshed_Morse_Code.smooshed_morse_code_2 import smalpha

testdata = [
    ".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..",
    ".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-",
    "..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-.."
]


@pytest.mark.parametrize("alpha_permutation", testdata)
def test_smalpha(alpha_permutation):
    assert_valid_smalpha(alpha_permutation, smalpha(alpha_permutation))


def assert_valid_smalpha(input_smorse, output_alpha):
    assert len(output_alpha) == 26
    assert smorse(output_alpha) == input_smorse
    assert "".join(sorted(output_alpha)) == "abcdefghijklmnopqrstuvwxyz"
