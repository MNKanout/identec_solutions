'''Unit test for the calculate_median function'''
import unittest
from .main import calculate_median


class TestMedian(unittest.TestCase):
    '''Represents test case for the calculate median function'''
    def test_median_odd(self):
        self.assertEqual(calculate_median([1, 2, 3]), 2)

    def test_median_even(self):
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)

    def test_median_duplicate(self):
        self.assertEqual(calculate_median([1, 2, 2, 3]), 2)

    def test_median_negative(self):
        self.assertEqual(calculate_median([-1, 0, 1]), 0)

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            calculate_median([])


if __name__ == '__main__':
    unittest.main()
