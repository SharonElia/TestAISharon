import unittest
from io import StringIO
import sys

class TestHello(unittest.TestCase):
    def test_calculation(self):
        b = 3 + 4
        self.assertEqual(b, 7)
    
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print("Sharon Test, world!")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Sharon Test, world!")

if __name__ == '__main__':
    unittest.main()
