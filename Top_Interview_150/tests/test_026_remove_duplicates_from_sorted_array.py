import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.remove_duplicates_from_sorted_array import Solution

class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 1, 2]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_case_2(self):
        nums = [0, 0, 1, 1, 1, 2, 3, 3, 4]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_case_3(self):
        nums = []
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_case_4(self):
        nums = [1, 2, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])

    def test_case_5(self):
        nums = [1, 1, 1, 1]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

if __name__ == "__main__":
    unittest.main()
   