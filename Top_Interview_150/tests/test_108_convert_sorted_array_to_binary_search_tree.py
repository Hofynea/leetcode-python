import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.convert_sorted_array_to_binary_search_tree import Solution, TreeNode, print_inorder

class TestSortedArrayToBST(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        root = s.sortedArrayToBST([-10, -3, 0, 5, 9])
        self.assertEqual(print_inorder(root), [-10, -3, 0, 5, 9])

    def test_case_2(self):
        s = Solution()
        root = s.sortedArrayToBST([1, 3])
        self.assertEqual(print_inorder(root), [1, 3])

if __name__ == "__main__":
    unittest.main()