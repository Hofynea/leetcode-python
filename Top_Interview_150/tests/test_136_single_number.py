import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.single_number import Solution

class TestSingleNumber(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 2, 1]
        self.assertEqual(Solution().singleNumber(nums), 1)

    def test_case_2(self):
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(Solution().singleNumber(nums), 4)

    def test_case_3(self):
        nums = [1]
        self.assertEqual(Solution().singleNumber(nums), 1)

if __name__ == "__main__":
    unittest.main()
