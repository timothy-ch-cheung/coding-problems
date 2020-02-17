import time

import pytest

from yahtzee_upper import yahtzee_upper


def test_should_return_10():
    assert yahtzee_upper([2, 3, 5, 5, 6]) == 10


def test_should_return_4():
    assert yahtzee_upper([1, 1, 1, 1, 4]) == 4


def test_should_return_6():
    assert yahtzee_upper([1, 1, 1, 3, 3]) == 6


def test_should_return_5():
    assert yahtzee_upper([1, 2, 3, 4, 5]) == 5


def test_should_return_30():
    assert yahtzee_upper([6, 6, 6, 6, 6]) == 30


def test_should_return_123456():
    dice_roll = [1654, 1654, 50995, 30864, 1654, 50995, 22747,
                                            1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
                                            30864, 4868, 30864]
    assert yahtzee_upper(dice_roll) == 123456

@pytest.mark.timeout(1)
def test_should_return_performance():
    with open('yahtzee-upper-1.txt') as f:
        lines = f.read().splitlines()
        lines = [int(x) for x in lines]
    start_time = time.time()
    actual = yahtzee_upper(lines)
    print(actual)
    time_taken = time.time() - start_time;
    assert actual == 123456
    assert time_taken < 0.2
