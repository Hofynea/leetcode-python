"""
222. Count Complete Tree Nodes
Category: Binary Tree General

Intuition:
We can exploit the structure of a complete binary tree. If the left and right subtree depths are equal, the left is a perfect tree and we can compute its node count directly.
Otherwise, the right subtree is perfect but one level smaller, and we recursively count nodes in the left subtree.

Approach:
- For each subtree, get the depth of the left and right branches.
- If depths match → left subtree is perfect → 2^depth - 1 nodes + recursive call on right.
- If depths differ → right subtree is perfect → 2^depth - 1 nodes + recursive call on left.
- Use bit shifting (1 << depth) instead of pow for speed.

Time Complexity:
O(log² n) – depth is O(log n), and we repeat the depth check at each level.

Space Complexity:
O(log n) – due to recursion depth in worst case.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        if left == right:
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)

    def getDepth(self, node: Optional[TreeNode]) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

if __name__ == "__main__":
    s = Solution()

    # Example 1: root = [1,2,3,4,5,6] → Output: 6
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)
    n1.left.left = TreeNode(4)
    n1.left.right = TreeNode(5)
    n1.right.left = TreeNode(6)
    print(s.countNodes(n1))  # 6

    # Example 2: root = [] → Output: 0
    print(s.countNodes(None))  # 0

    # Example 3: root = [1] → Output: 1
    n2 = TreeNode(1)
    print(s.countNodes(n2))  # 1
