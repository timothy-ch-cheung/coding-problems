import unittest

from yahtzee_upper import get_score


class MyTestCase(unittest.TestCase):
    def test_get_score_should_return_6(self):
        self.assertEqual(6, get_score([2, 3, 5, 5, 6], 6))

    def test_get_score_should_return_10(self):
        self.assertEqual(10, get_score([2, 3, 5, 5, 6], 5))

    def test_get_score_should_return_18(self):
        self.assertEqual(18, get_score([6, 6, 5, 5, 6], 6))

    def test_get_score_should_not_error(self):
        self.assertEqual(0, get_score([6, 6, 5, 5, 6], 2))


if __name__ == '__main__':
    unittest.main()
