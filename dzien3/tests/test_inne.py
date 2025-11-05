import unittest


def divide(a, b):
    return a / b


# PascalCase
class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()
