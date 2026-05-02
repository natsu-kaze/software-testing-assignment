import unittest
from check_age import check_age


class TestCheckAge(unittest.TestCase):

    def test_age_below_18_minor(self):
        self.assertEqual(check_age(0), "未成年")
        self.assertEqual(check_age(17), "未成年")
        self.assertEqual(check_age(-1), "未成年")

    def test_age_18_adult(self):
        self.assertEqual(check_age(18), "成年")

    def test_age_19_to_60_adult(self):
        self.assertEqual(check_age(19), "成年")
        self.assertEqual(check_age(30), "成年")
        self.assertEqual(check_age(60), "成年")

    def test_age_above_60_elderly(self):
        self.assertEqual(check_age(61), "老年")
        self.assertEqual(check_age(100), "老年")


if __name__ == '__main__':
    unittest.main()