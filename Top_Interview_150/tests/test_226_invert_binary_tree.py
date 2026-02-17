import unittest
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.invert_binary_tree import Solution, TreeNode


class TestInvertBinaryTree(unittest.TestCase):

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

    def tree_to_list(self, root):
        if not root:
            return []

        from collections import deque
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    # Official LeetCode Example 1
    def test_case_1(self):
        root = self.build_tree([4, 2, 7, 1, 3, 6, 9])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [4, 7, 2, 9, 6, 3, 1])

    # Official LeetCode Example 2
    def test_case_2(self):
        root = self.build_tree([2, 1, 3])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [2, 3, 1])

    # Official LeetCode Example 3
    def test_case_3(self):
        root = self.build_tree([])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [])

    # Single node
    def test_case_4(self):
        root = self.build_tree([1])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1])

    # Two nodes (left only)
    def test_case_5(self):
        root = self.build_tree([1, 2])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, None, 2])

    # Two nodes (right only)
    def test_case_6(self):
        root = self.build_tree([1, None, 2])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, 2])

    # Left skewed tree
    def test_case_7(self):
        root = self.build_tree([1, 2, None, 3])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, None, 2, None, 3])

    # Right skewed tree
    def test_case_8(self):
        root = self.build_tree([1, None, 2, None, 3])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, 2, None, 3])

    # Negative values
    def test_case_9(self):
        root = self.build_tree([0, -1, -2])
        inverted = Solution().invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [0, -2, -1])

    # Larger tree
    def test_case_10(self):
        root = self.build_tree([1,2,3,4,5,6,7,8,9])
        inverted = Solution().invertTree(root)
        self.assertEqual(
            self.tree_to_list(inverted),
            [1,3,2,7,6,5,4,None,None,None,None,None,None,9,8]
        )

    # Already symmetric structure (inverting gives same level-order)
    def test_case_11(self):
        root = self.build_tree([1,2,2,3,4,4,3])
        inverted = Solution().invertTree(root)
        self.assertEqual(
            self.tree_to_list(inverted),
            [1,2,2,3,4,4,3]  # symmetric tree: swap left/right yields same structure
        )


if __name__ == "__main__":
    unittest.main()