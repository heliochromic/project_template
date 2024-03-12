import unittest
from unittest.mock import patch
import pandas as pd
from app.io.input import input_text, read_file, read_csv_with_pandas


class InputFunctionsTest(unittest.TestCase):

    @patch('builtins.input', return_value='Test input')
    def test_input_text(self, mock_input):
        result = input_text()
        self.assertEqual(result, 'Test input')

    def test_read_file_existing_file(self):
        content = "some random text"
        filename = "test_file.txt"
        with open(filename, 'w') as file:
            file.write(content)

        result = read_file(filename)
        self.assertEqual(result, content)




if __name__ == '__main__':
    unittest.main()
