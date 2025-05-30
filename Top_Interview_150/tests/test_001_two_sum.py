import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(Solution().twoSum(nums, target), [0, 1])

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(Solution().twoSum(nums, target), [1, 2])

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(Solution().twoSum(nums, target), [0, 1])

    def test_case_4(self):
        nums = [1, 5, 3, 7]
        target = 10
        self.assertEqual(Solution().twoSum(nums, target), [2, 3])

    def test_case_5(self):
        nums = [1, 2, 3, 4, 5]
        target = 9
        self.assertEqual(Solution().twoSum(nums, target), [3, 4])

if __name__ == "__main__":
    unittest.main()
    