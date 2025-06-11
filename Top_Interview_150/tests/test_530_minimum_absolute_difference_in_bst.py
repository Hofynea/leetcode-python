import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.minimum_absolute_difference_in_bst import Solution, TreeNode

class TestMinimumAbsDiffBST(unittest.TestCase):
    def test_case_1(self):
        # Tree: [4,2,6,1,3]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(Solution().getMinimumDifference(root), 1)

    def test_case_2(self):
        # Tree: [1,0,48,null,null,12,49]
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)
        self.assertEqual(Solution().getMinimumDifference(root), 1)

if __name__ == "__main__":
    unittest.main()
    