import unittest
from calculator import add, is_positive, sqrt, NegativeNumberError


class TestCalculator(unittest.TestCase):

    def test_add_assertEqual(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(100, 200), 300)

    def test_is_positive_assertTrue(self):
        self.assertTrue(is_positive(1))
        self.assertTrue(is_positive(0.01))
        self.assertTrue(is_positive(100))

    def test_is_positive_assertFalse(self):
        self.assertFalse(is_positive(-1))
        self.assertFalse(is_positive(-0.01))
        self.assertFalse(is_positive(0))

    def test_sqrt_assertAlmostEqual(self):
        self.assertAlmostEqual(sqrt(4), 2.0)
        self.assertAlmostEqual(sqrt(2), 1.414, places=3)

    def test_sqrt_assertRaises(self):
        self.assertRaises(NegativeNumberError, sqrt, -1)
        self.assertRaises(NegativeNumberError, sqrt, -100)


if __name__ == '__main__':
    unittest.main()

    