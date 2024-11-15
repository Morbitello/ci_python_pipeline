import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Inizializza l'oggetto Calculator prima di ogni test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test per la somma."""
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self):
        """Test per la sottrazione."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        """Test per la moltiplicazione."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        """Test per la divisione."""
        self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_divide_by_zero(self):
        """Test per la divisione per zero."""
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
