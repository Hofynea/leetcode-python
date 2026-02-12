import unittest
import sys
import os
from typing import Optional
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.symmetric_tree import Solution, TreeNode


class TestSymmetricTree(unittest.TestCase):

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
        # Input: [1,2,2,3,4,4,3]
        root = self.build_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(Solution().isSymmetric(root))

    def test_case_2(self):
        # Input: [1,2,2,None,3,None,3]
        root = self.build_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(Solution().isSymmetric(root))

    def test_case_3(self):
        # Input: [1]
        root = self.build_tree([1])
        self.assertTrue(Solution().isSymmetric(root))

    def test_case_4(self):
        # Input: []
        root = self.build_tree([])
        self.assertTrue(Solution().isSymmetric(root))

    def test_case_5(self):
        # Input: [1,2,2,3,None,None,4]
        root = self.build_tree([1, 2, 2, 3, None, None, 4])
        self.assertFalse(Solution().isSymmetric(root))


if __name__ == "__main__":
    unittest.main()