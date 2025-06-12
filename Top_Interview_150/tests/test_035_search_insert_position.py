import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.search_insert_position import Solution

class TestSearchInsertPosition(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_case_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_case_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected = 4
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_case_4(self):
        nums = [1]
        target = 0
        expected = 0
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_case_5(self):
        nums = [1]
        target = 2
        expected = 1
        self.assertEqual(Solution().searchInsert(nums, target), expected)

if __name__ == "__main__":
    unittest.main()
    