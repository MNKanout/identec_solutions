'''Unit test for a function that counts digit '2' in numbers from 1 to n'''
import unittest
from main import count_digit_two


class TestCountDigitTwo(unittest.TestCase):
    '''Represents the test case for the count_digit_two function'''
    def test_single_number(self):
        '''Test with a single number'''
        self.assertEqual(count_digit_two(1), 0)

    def test_count_twos_two(self):
        '''Test with two numbers'''
        self.assertEqual(count_digit_two(2), 1)

    def test_count_twos_small(self):
        '''Test with a small range of numbers'''
        self.assertEqual(count_digit_two(30), 13)

    def test_count_twos_medium(self):
        '''Test with a medium range of numbers'''
        self.assertEqual(count_digit_two(100), 20)

    def test_count_twos_large(self):
        '''Test with a large range of numbers'''
        self.assertEqual(count_digit_two(1000), 300)

    def test_count_twos_zero(self):
        '''Test with zero as a given argument'''
        with self.assertRaises(ValueError):
            count_digit_two(0)

    def test_count_twos_empty(self):
        '''Test with an None argument'''
        with self.assertRaises(ValueError):
            count_digit_two(None)

    def test_count_twos_negative(self):
        '''Test with a negative argument'''
        with self.assertRaises(ValueError):
            count_digit_two(-1)


if __name__ == '__main__':
    unittest.main()
