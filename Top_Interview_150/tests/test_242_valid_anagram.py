import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.valid_anagram import Solution

class TestValidAnagram(unittest.TestCase):
    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(Solution().isAnagram(s, t))

    def test_case_2(self):
        s = "rat"
        t = "car"
        self.assertFalse(Solution().isAnagram(s, t))

    def test_case_3(self):
        s = "a"
        t = "a"
        self.assertTrue(Solution().isAnagram(s, t))

    def test_case_4(self):
        s = "ab"
        t = "ba"
        self.assertTrue(Solution().isAnagram(s, t))

    def test_case_5(self):
        s = "abc"
        t = "cba"
        self.assertTrue(Solution().isAnagram(s, t))

    def test_case_6(self):
        s = "aacc"
        t = "ccac"
        self.assertFalse(Solution().isAnagram(s, t))

    def test_case_7(self):
        s = ""
        t = ""
        self.assertTrue(Solution().isAnagram(s, t))  # Edge case: both empty

if __name__ == "__main__":
    unittest.main()
    