import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.maximum_depth_of_binary_tree import Solution, TreeNode

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_case_1(self):
        # Input: [3, 9, 20, None, None, 15, 7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        result = Solution().maxDepth(root)
        self.assertEqual(result, 3)

    def test_case_2(self):
        # Input: [1, None, 2]
        root = TreeNode(1)
        root.right = TreeNode(2)

        result = Solution().maxDepth(root)
        self.assertEqual(result, 2)

    def test_case_3(self):
        # Single node
        root = TreeNode(5)

        result = Solution().maxDepth(root)
        self.assertEqual(result, 1)

    def test_case_4(self):
        # Empty tree
        root = None

        result = Solution().maxDepth(root)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()