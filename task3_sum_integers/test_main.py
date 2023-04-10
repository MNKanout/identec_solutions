import unittest
# Local modules
from main import get_integers_from_file, sum_integers

SAMPLES_DIR = 'test_samples/'


class TestGetIntegersFromFile(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            get_integers_from_file("nonexistent_file.txt")

    def test_integers_file(self):
        self.assertEqual(get_integers_from_file(
            SAMPLES_DIR+'num_1_10.txt'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class TestSumIntegersFromFile(unittest.TestCase):

    def test_empty_file(self):
        self.assertEqual(sum_integers(SAMPLES_DIR+'empty.txt'), 0)

    def test_small_range(self):
        self.assertEqual(sum_integers(SAMPLES_DIR+'num_1_20.txt'), 210)

    def test_medium_range(self):
        self.assertEqual(sum_integers(SAMPLES_DIR+'num_1_100.txt'), 5050)

    def test_large_range(self):
        self.assertEqual(sum_integers(SAMPLES_DIR+'num_1_500.txt'), 125250)

    def test_int_floats_numbers(self):
        self.assertEqual(sum_integers(SAMPLES_DIR+'int_floats.txt'), 985)

    def test_negative_int(self):
        self.assertEqual(sum_integers(SAMPLES_DIR+'negative_int.txt'), -87)


if __name__ == '__main__':
    unittest.main()
