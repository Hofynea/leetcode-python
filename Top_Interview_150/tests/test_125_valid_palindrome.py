import unittest
import sys
import os

# Ensure we can import from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.valid_palindrome import Solution  # Adjust path if needed

class TestValidPalindrome(unittest.TestCase):
    def test_case_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(Solution().isPalindrome(s))

    def test_case_2(self):
        s = "race a car"
        self.assertFalse(Solution().isPalindrome(s))

    def test_case_3(self):
        s = " "
        self.assertTrue(Solution().isPalindrome(s))

    def test_case_4(self):
        s = "No lemon, no melon"
        self.assertTrue(Solution().isPalindrome(s))

    def test_case_5(self):
        s = "Was it a car or a cat I saw?"
        self.assertTrue(Solution().isPalindrome(s))


if __name__ == "__main__":
    unittest.main()
    