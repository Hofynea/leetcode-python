import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.contains_duplicate_II import Solution

class TestContainsNearbyDuplicate(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 1]
        k = 3
        self.assertTrue(Solution().containsNearbyDuplicate(nums, k))

    def test_case_2(self):
        nums = [1, 0, 1, 1]
        k = 1
        self.assertTrue(Solution().containsNearbyDuplicate(nums, k))

    def test_case_3(self):
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        self.assertFalse(Solution().containsNearbyDuplicate(nums, k))

    def test_case_4(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        self.assertFalse(Solution().containsNearbyDuplicate(nums, k))

if __name__ == "__main__":
    unittest.main()
    