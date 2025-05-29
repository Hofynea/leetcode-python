import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.word_pattern import Solution

class TestWordPattern(unittest.TestCase):
    def test_case_1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        self.assertTrue(Solution().wordPattern(pattern, s))

    def test_case_2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        self.assertFalse(Solution().wordPattern(pattern, s))

    def test_case_3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        self.assertFalse(Solution().wordPattern(pattern, s))

    def test_case_4(self):
        pattern = "abc"
        s = "dog cat fish"
        self.assertTrue(Solution().wordPattern(pattern, s))

    def test_case_5(self):
        pattern = "abc"
        s = "dog dog dog"
        self.assertFalse(Solution().wordPattern(pattern, s))

    def test_case_6(self):
        pattern = "ab"
        s = "dog"
        self.assertFalse(Solution().wordPattern(pattern, s))  # length mismatch

    def test_case_7(self):
        pattern = ""
        s = ""
        self.assertTrue(Solution().wordPattern(pattern, s))  # edge case

if __name__ == "__main__":
    unittest.main()
    