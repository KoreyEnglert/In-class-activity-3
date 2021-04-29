import unittest
import calculator

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 10), 15);
        self.assertEqual(calculator.add(5, 9), 15);

    def test_sub(self):
        self.assertEqual(calculator.sub(5, 10), -5);
        self.assertEqual(calculator.sub(5, 9), -5);

    def test_mul(self):
        self.assertEqual(calculator.mul(5, 10), 50);
        self.assertEqual(calculator.mul(5, 9), 50);

    def test_div(self):
        self.assertAlmostEqual(calculator.div(5, 10), .5);
        self.assertAlmostEqual(calculator.div(5, 9), .5);
