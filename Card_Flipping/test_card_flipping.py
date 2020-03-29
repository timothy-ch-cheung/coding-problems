import pytest

from Card_Flipping.card_flipping import solve_cards

testdata = [
    ("0100110", [1, 0, 2, 3, 5, 4, 6]),
    ("01001100111", None),
    ("100001100101000", [0, 1, 2, 3, 4, 6, 5, 7, 8, 11, 10, 9, 12, 13, 14])
]


@pytest.mark.parametrize("cards,,expected", testdata)
def test_smalpha(cards, expected):
    assert solve_cards(cards) == expected
