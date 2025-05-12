import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.isomorphic_strings import Solution

class TestIsomorphicStrings(unittest.TestCase):
    def test_case_1(self):
        s = "egg"
        t = "add"
        self.assertTrue(Solution().isIsomorphic(s, t))

    def test_case_2(self):
        s = "foo"
        t = "bar"
        self.assertFalse(Solution().isIsomorphic(s, t))

    def test_case_3(self):
        s = "paper"
        t = "title"
        self.assertTrue(Solution().isIsomorphic(s, t))

    def test_case_4(self):
        s = "ab"
        t = "aa"
        self.assertFalse(Solution().isIsomorphic(s, t))

    def test_case_5(self):
        s = "badc"
        t = "baba"
        self.assertFalse(Solution().isIsomorphic(s, t))

    def test_case_6(self):
        s = "a"
        t = "a"
        self.assertTrue(Solution().isIsomorphic(s, t))

    def test_case_7(self):
        s = "abc"
        t = "def"
        self.assertTrue(Solution().isIsomorphic(s, t))

    def test_case_8(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        t = "zyxwvutsrqponmlkjihgfedcba"
        self.assertTrue(Solution().isIsomorphic(s, t))

if __name__ == "__main__":
    unittest.main()
    