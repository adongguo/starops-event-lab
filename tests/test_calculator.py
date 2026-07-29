import unittest

from app.calculator import add, subtract


class CalculatorTest(unittest.TestCase):
    def test_adds_two_integers(self) -> None:
        self.assertEqual(3, add(1, 2))

    def test_subtracts_two_integers(self) -> None:
        self.assertEqual(2, subtract(5, 3))


if __name__ == "__main__":
    unittest.main()
