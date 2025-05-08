import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.longest_common_prefix import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def test_case_1(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "fl")

    def test_case_2(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "")

    def test_case_3(self):
        strs = ["interview", "internet", "internal"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "inter")

    def test_case_4(self):
        strs = ["a"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "a")

    def test_case_5(self):
        strs = ["prefix", "prefixing", "prefixes"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "prefix")

if __name__ == "__main__":
    unittest.main()
