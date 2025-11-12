"""
100. Same Tree
Category: Binary Tree General

Intuition:
Use recursion to compare both trees node by node. If both nodes are None, they are the same.
If only one is None, or their values differ, they are not the same.

Approach:
- If p and q are both None → return True
- If one is None → return False
- If values differ → return False
- Recursively check left and right children

Time Complexity:
O(n) – must visit every node in both trees.

Space Complexity:
O(h) – where h is the height of the tree due to recursion stack.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    s = Solution()

    # Example 1: Input: [1,2,3], [1,2,3] → Output: True
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    print(s.isSameTree(p1, q1))  # True

    # Example 2: Input: [1,2], [1,null,2] → Output: False
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    print(s.isSameTree(p2, q2))  # False

    # Example 3: Input: [1,2,1], [1,1,2] → Output: False
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)
    print(s.isSameTree(p3, q3))  # False

    # Both trees are None
    print(s.isSameTree(None, None))  # True

    # One tree is None, the other is not
    print(s.isSameTree(TreeNode(0), None))  # False