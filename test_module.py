import unittest

from module import MyClass, Api


class MyClassTestCase(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(MyClass.sum(1, 3), 4)

    def test_sum_negative_positive(self):
        self.assertEqual(MyClass.sum(-1, 2), 1)

    def test_sum_negative(self):
        self.assertEqual(MyClass.sum(-3, -1), -4)


class ApiTestCase(unittest.TestCase):
    def test_formatted_users(self):
        api = Api()
        api.create_user('John')
        formatted_users = api.get_formatted_users()
        expected_formatted_users = '1: John'
        self.assertEqual(formatted_users, expected_formatted_users)
