import os
import unittest
from int_file_gen import generate_integers_file


class TestGenerateIntegersFile(unittest.TestCase):
    def setUp(self):
        '''Create a temporary file before running the test'''
        self.file_name = 'test_integers.txt'  # File name.
        self.file_path = os.path.join(os.getcwd(), self.file_name)  # File path

    def tearDown(self):
        '''Remove created file after running the test'''
        os.remove(self.file_path)

    def test_generate_integers_file(self):
        generate_integers_file(self.file_name, 5)
        with open(self.file_path, 'r') as f:
            contents = f.readlines()
        expected_output = ['1\n', '2\n', '3\n', '4\n', '5\n']
        self.assertEqual(contents, expected_output)


if __name__ == '__main__':
    unittest.main()
