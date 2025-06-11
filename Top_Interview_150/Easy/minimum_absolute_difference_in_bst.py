"""
530. Minimum Absolute Difference in BST
Category: Binary Search Tree

Intuition:
In a BST, an in-order traversal visits nodes in sorted order.
To find the minimum absolute difference, we:
- Traverse in order
- Compare current node with the previous node
- Track the smallest difference

Approach:
- Initialize:
  - prev = None to track the previous node's value
  - min_diff = infinity to track the smallest difference
- Perform in-order traversal:
  - For each node:
    - If prev exists, update min_diff = min(min_diff, node.val - prev)
    - Set prev = node.val
- Return min_diff

Time Complexity:
O(n), we visit each node once.

Space Complexity:
O(h), h = height of tree (recursion stack).

Example:
Input: root = [4,2,6,1,3]
Output: 1
Explanation: Minimum absolute difference is |3 - 2| = 1
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff

if __name__ == "__main__":
    def build_tree_from_list(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    s = Solution()
    root1 = build_tree_from_list([4, 2, 6, 1, 3])
    print(s.getMinimumDifference(root1))  # Expected: 1

    root2 = build_tree_from_list([1, 0, 48, None, None, 12, 49])
    print(s.getMinimumDifference(root2))  # Expected: 1
