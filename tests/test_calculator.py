import unittest

from app.calculator import add


class CalculatorTest(unittest.TestCase):
    def test_adds_two_integers(self) -> None:
        self.assertEqual(3, add(1, 2))


if __name__ == "__main__":
    unittest.main()
