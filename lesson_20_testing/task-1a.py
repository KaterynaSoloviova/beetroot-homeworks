# Task 1
# Pick your solution to one of the exercises in this module. Design tests for this solution and write tests
# using unittest library.

from fraction import Fraction
import unittest


class TestFraction(unittest.TestCase):
    def test_add_positive(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)

        res = x + y
        expected = Fraction(7, 6)

        self.assertEqual(str(res), str(expected))

    def test_add_negative(self):
        x = Fraction(-5, 7)
        y = Fraction(3, 5)

        res = x + y
        expected = Fraction(-4, 35)

        self.assertEqual(str(res), str(expected))

    def test_sub_positive(self):
        x = Fraction(3, 7)
        y = Fraction(1, 3)

        res = x - y
        expected = Fraction(2, 21)

        self.assertEqual(str(res), str(expected))

    def test_sub_negative_minuend(self):
        x = Fraction(-3, 5)
        y = Fraction(1, 5)

        res = x - y
        expected = Fraction(-4, 5)

        self.assertEqual(str(res), str(expected))

    def test_sub_negative_subtrahend(self):
        x = Fraction(2, 5)
        y = Fraction(-1, 3)

        res = x - y
        expected = Fraction(11, 15)

        self.assertEqual(str(res), str(expected))

    def test_mul_positive(self):
        x = Fraction(3, 5)
        y = Fraction(2, 3)

        res = x * y
        expected = Fraction(6, 15)

        self.assertEqual(str(res), str(expected))

    def test_mul_negative(self):
        x = Fraction(-3, 5)
        y = Fraction(2, 3)

        res = x * y
        expected = Fraction(-6, 15)

        self.assertEqual(str(res), str(expected))

    def test_truediv_positive(self):
        x = Fraction(6, 31)
        y = Fraction(2, 3)

        res = x / y
        expected = Fraction(9, 31)

    def test_truediv_negative(self):
        x = Fraction(2, 3)
        y = Fraction(-2, 3)

        res = x / y
        expected = Fraction(1, -1)

        self.assertEqual(str(res), str(expected))

    def test_truediv_zero(self):
        x = Fraction(2, 3)
        y = Fraction(0, 2)

        try:
            res = x / y
        except ZeroDivisionError as e:
            self.assertEqual(str(e), "Cannot divide by zero")
        else:
            raise AssertionError("Expected error: divide by zero")

    def test_fraction_reduction(self):
        x = Fraction(18, 42)

        expected = Fraction(3, 7)

        self.assertEqual(str(x), str(expected))


if __name__ == "__main__":
    unittest.main()
