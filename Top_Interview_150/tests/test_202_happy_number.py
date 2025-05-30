import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.happy_number import Solution

class TestHappyNumber(unittest.TestCase):
    def test_case_1(self):
        n = 19
        self.assertTrue(Solution().isHappy(n))

    def test_case_2(self):
        n = 2
        self.assertFalse(Solution().isHappy(n))

    def test_case_3(self):
        n = 1
        self.assertTrue(Solution().isHappy(n))

    def test_case_4(self):
        n = 116
        self.assertFalse(Solution().isHappy(n))

if __name__ == "__main__":
    unittest.main()
