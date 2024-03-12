import unittest
from unittest.mock import patch
import pandas as pd
from app.io.input import input_text, read_file, read_csv_with_pandas


class InputFunctionsTest(unittest.TestCase):

    @patch('builtins.input', return_value='Test input')
    def test_input_text(self, mock_input):
        result = input_text()
        self.assertEqual(result, 'Test input')




if __name__ == '__main__':
    unittest.main()
