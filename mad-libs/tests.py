import unittest
from unittest.mock import patch  # Importing patch from unittest.mock to mock user input
from io import StringIO  # Importing StringIO to capture printed output
from main import mad_libs  # Importing the mad_libs function from main.py

class TestMadLibs(unittest.TestCase):
    @patch('builtins.input', side_effect=['funny', 'cat', 'danced', 'happily'])  # Patching the input() function with mock values
    @patch('sys.stdout', new_callable=StringIO)  # Patching sys.stdout to capture printed output
    def test_mad_libs(self, mock_stdout, mock_input):
        mad_libs()  # Calling the mad_libs function with mock user input
        expected_output = "Once upon a time, there was a funny cat who danced happily.\n"  # Expected output based on mock input
        self.assertEqual(mock_stdout.getvalue(), expected_output)  # Asserting that the printed output matches the expected output

if __name__ == "__main__":
    unittest.main()
