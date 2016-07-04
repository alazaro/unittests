import unittest

from module import MyClass


class MyClassTestCase(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(MyClass.sum(1, 3), 4)

    def test_sum_negative_positive(self):
        self.assertEqual(MyClass.sum(-1, 2), 1)

    def test_sum_negative(self):
        self.assertEqual(MyClass.sum(-3, -1), -4)
