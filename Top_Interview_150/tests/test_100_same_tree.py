import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.same_tree import Solution, TreeNode

class TestSameTree(unittest.TestCase):

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
        # Input: p = [1,2,3], q = [1,2,3]
        p = self.build_tree([1, 2, 3])
        q = self.build_tree([1, 2, 3])
        self.assertTrue(Solution().isSameTree(p, q))

    def test_case_2(self):
        # Input: p = [1,2], q = [1,null,2]
        p = self.build_tree([1, 2])
        q = self.build_tree([1, None, 2])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_case_3(self):
        # Input: p = [1,2,1], q = [1,1,2]
        p = self.build_tree([1, 2, 1])
        q = self.build_tree([1, 1, 2])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_case_4(self):
        # Input: p = None, q = None
        self.assertTrue(Solution().isSameTree(None, None))

    def test_case_5(self):
        # Input: p = [0], q = None
        p = TreeNode(0)
        q = None
        self.assertFalse(Solution().isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()