import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.is_subsequence import Solution

class TestIsSubsequence(unittest.TestCase):
    def test_case_1(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(Solution().isSubsequence(s, t))

    def test_case_2(self):
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(Solution().isSubsequence(s, t))

    def test_case_3(self):
        s = ""
        t = "ahbgdc"
        self.assertTrue(Solution().isSubsequence(s, t))

    def test_case_4(self):
        s = "abc"
        t = ""
        self.assertFalse(Solution().isSubsequence(s, t))

    def test_case_5(self):
        s = "aaaaaa"
        t = "bbaaaa"
        self.assertFalse(Solution().isSubsequence(s, t))

if __name__ == "__main__":
    unittest.main()
    