import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Medium.remove_duplicates_from_sorted_array_II import Solution

class TestRemoveDuplicatesFromSortedArrayII(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 1, 2, 2, 3])

    def test_case_2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0, 0, 1, 1, 2, 3, 3])

    def test_case_3(self):
        nums = [1, 2, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])

    def test_case_4(self):
        nums = [1, 1, 1]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 1])

    def test_case_5(self):
        nums = []
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

if __name__ == "__main__":
    unittest.main()
