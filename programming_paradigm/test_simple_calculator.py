import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Create an instance of SimpleCalculator for testing."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)          # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)         # Negative and positive
        self.assertEqual(self.calc.add(-1, -1), -2)       # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)           # Zero case

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)    # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)    # Negative result
        self.assertEqual(self.calc.subtract(-1, -1), 0)   # Zero result
        self.assertEqual(self.calc.subtract(0, 1), -1)     # Zero as first operand

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)     # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)    # Negative and positive
        self.assertEqual(self.calc.multiply(-1, -1), 1)    # Negative numbers
        self.assertEqual(self.calc.multiply(0, 100), 0)     # Zero case

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)       # Normal case
        self.assertEqual(self.calc.divide(-1, 1), -1)      # Negative and positive
        self.assertEqual(self.calc.divide(-1, -1), 1)      # Negative numbers
        self.assertIsNone(self.calc.divide(1, 0))          # Division by zero case

if __name__ == '__main__':
    unittest.main()