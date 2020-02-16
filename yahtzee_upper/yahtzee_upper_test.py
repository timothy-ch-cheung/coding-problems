import unittest
import time

from yahtzee_upper import yahtzee_upper


class MyTestCase(unittest.TestCase):
    def test_should_return_10(self):
        self.assertEqual(10, yahtzee_upper([2, 3, 5, 5, 6]))

    def test_should_return_4(self):
        self.assertEqual(4, yahtzee_upper([1, 1, 1, 1, 4]))

    def test_should_return_6(self):
        self.assertEqual(6, yahtzee_upper([1, 1, 1, 3, 3]))

    def test_should_return_5(self):
        self.assertEqual(5, yahtzee_upper([1, 2, 3, 4, 5]))

    def test_should_return_30(self):
        self.assertEqual(30, yahtzee_upper([6, 6, 6, 6, 6]))

    def test_should_return_30(self):
        self.assertEqual(30, yahtzee_upper([6, 6, 6, 6, 6]))

    def test_should_return_123456(self):
        self.assertEqual(123456, yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
                                                1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
                                                30864, 4868, 30864]))

    def test_should_return_123456_performance(self):
        start_time = time.time()
        actual = yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
                                                1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
                                                30864, 4868, 30864])
        time_taken = time.time() - start_time;
        self.assertEqual(123456, actual)
        self.assertTrue(time_taken < 0.2)


if __name__ == '__main__':
    unittest.main()
