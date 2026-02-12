import unittest
import sys
import os
from typing import Optional
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.path_sum import Solution, TreeNode

class TestPathSum(unittest.TestCase):

    def build_tree(self, vals):
        if not vals:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def test_case_1(self):
        # Input: [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
        root = self.build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        target = 22
        self.assertTrue(Solution().hasPathSum(root, target))

    def test_case_2(self):
        # Input: [1,2,3], targetSum = 5
        root = self.build_tree([1, 2, 3])
        target = 5
        self.assertFalse(Solution().hasPathSum(root, target))

    def test_case_3(self):
        # Input: [], targetSum = 0
        root = self.build_tree([])
        target = 0
        self.assertFalse(Solution().hasPathSum(root, target))

    def test_case_4(self):
        # Input: [1,2], targetSum = 0
        root = self.build_tree([1, 2])
        target = 0
        self.assertFalse(Solution().hasPathSum(root, target))

    def test_case_5(self):
        # Input: [1,2], targetSum = 3
        root = self.build_tree([1, 2])
        target = 3
        self.assertTrue(Solution().hasPathSum(root, target))

if __name__ == "__main__":
    unittest.main()