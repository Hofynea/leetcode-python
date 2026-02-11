import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.count_complete_tree_nodes import Solution, TreeNode

class TestCountCompleteTreeNodes(unittest.TestCase):

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
        # Input: [1,2,3,4,5,6], Output: 6
        root = self.build_tree([1, 2, 3, 4, 5, 6])
        self.assertEqual(Solution().countNodes(root), 6)

    def test_case_2(self):
        # Input: [], Output: 0
        root = self.build_tree([])
        self.assertEqual(Solution().countNodes(root), 0)

    def test_case_3(self):
        # Input: [1], Output: 1
        root = self.build_tree([1])
        self.assertEqual(Solution().countNodes(root), 1)

    def test_case_4(self):
        # Input: [1, 2, 3, 4, 5, 6, 7, 8], Output: 8
        root = self.build_tree([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(Solution().countNodes(root), 8)

    def test_case_5(self):
        # Input: [1, 2, 3, 4, 5], Output: 5
        root = self.build_tree([1, 2, 3, 4, 5])
        self.assertEqual(Solution().countNodes(root), 5)


if __name__ == "__main__":
    unittest.main()