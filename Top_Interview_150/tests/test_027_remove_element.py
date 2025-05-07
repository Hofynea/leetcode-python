import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.remove_element import Solution

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = Solution().removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertCountEqual(nums[:k], [2, 2])

    def test_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = Solution().removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertCountEqual(nums[:k], [0, 1, 3, 0, 4])

    def test_case_3(self):
        nums = [1]
        val = 1
        k = Solution().removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_case_4(self):
        nums = [1]
        val = 2
        k = Solution().removeElement(nums, val)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test_case_5(self):
        nums = []
        val = 0
        k = Solution().removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

if __name__ == "__main__":
    unittest.main()
    