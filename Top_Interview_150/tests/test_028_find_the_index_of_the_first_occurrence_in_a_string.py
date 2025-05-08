import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.find_the_index_of_the_first_occurrence_in_a_string import Solution

class TestFindIndexOfFirstOccurrence(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().strStr("sadbutsad", "sad"), 0)

    def test_case_2(self):
        self.assertEqual(Solution().strStr("leetcode", "leeto"), -1)

    def test_case_3(self):
        self.assertEqual(Solution().strStr("hello", "ll"), 2)

    def test_case_4(self):
        self.assertEqual(Solution().strStr("aaaaa", "bba"), -1)

    def test_case_5(self):
        self.assertEqual(Solution().strStr("aaa", "a"), 0)

if __name__ == "__main__":
    unittest.main()
