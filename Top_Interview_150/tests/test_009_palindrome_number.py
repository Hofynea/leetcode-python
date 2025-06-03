import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.palindrome_number import Solution

class TestPalindromeNumber(unittest.TestCase):
    def test_case_1(self):
        x = 121
        self.assertTrue(Solution().isPalindrome(x))

    def test_case_2(self):
        x = -121
        self.assertFalse(Solution().isPalindrome(x))

    def test_case_3(self):
        x = 10
        self.assertFalse(Solution().isPalindrome(x))

    def test_case_4(self):
        x = 0
        self.assertTrue(Solution().isPalindrome(x))

    def test_case_5(self):
        x = 12321
        self.assertTrue(Solution().isPalindrome(x))

if __name__ == "__main__":
    unittest.main()
    