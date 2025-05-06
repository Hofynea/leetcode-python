import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.merge_sorted_array import Solution

class TestMergeSortedArray(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        Solution().merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_case_2(self):
        nums1 = [1]
        nums2 = []
        Solution().merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

    def test_case_3(self):
        nums1 = [0]
        nums2 = [1]
        Solution().merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

if __name__ == "__main__":
    unittest.main()
    