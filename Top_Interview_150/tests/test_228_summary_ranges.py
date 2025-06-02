import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.summary_ranges import Solution

class TestSummaryRanges(unittest.TestCase):
    def test_case_1(self):
        nums = [0, 1, 2, 4, 5, 7]
        expected = ["0->2", "4->5", "7"]
        self.assertEqual(Solution().summaryRanges(nums), expected)

    def test_case_2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        expected = ["0", "2->4", "6", "8->9"]
        self.assertEqual(Solution().summaryRanges(nums), expected)

    def test_case_3(self):
        nums = []
        expected = []
        self.assertEqual(Solution().summaryRanges(nums), expected)

    def test_case_4(self):
        nums = [5]
        expected = ["5"]
        self.assertEqual(Solution().summaryRanges(nums), expected)

if __name__ == "__main__":
    unittest.main()
    