import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.majority_element import Solution

class TestMajorityElement(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 2, 3]
        self.assertEqual(Solution().majorityElement(nums), 3)

    def test_case_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(Solution().majorityElement(nums), 2)

    def test_case_3(self):
        nums = [1]
        self.assertEqual(Solution().majorityElement(nums), 1)

    def test_case_4(self):
        nums = [6, 5, 5]
        self.assertEqual(Solution().majorityElement(nums), 5)

    def test_case_5(self):
        nums = [9, 9, 9, 1, 2, 3, 9, 4, 9, 5, 9]
        self.assertEqual(Solution().majorityElement(nums), 9)

if __name__ == "__main__":
    unittest.main()
