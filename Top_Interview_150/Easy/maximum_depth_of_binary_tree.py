"""
104. Maximum Depth of Binary Tree
Category: Binary Tree General

Intuition:
Use recursion to find the depth of left and right subtrees, and return the max of the two plus 1 (for the current node).

Approach:
- If the current node is None, return 0.
- Otherwise, return 1 + max(depth of left, depth of right).

Time Complexity:
- O(n) — visit every node once.

Space Complexity:
- O(h) — height of the tree (due to recursion stack).
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    # Sample input: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().maxDepth(root))  # Output: 3