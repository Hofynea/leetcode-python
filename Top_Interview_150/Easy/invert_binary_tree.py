"""
226. Invert Binary Tree
Category: Binary Tree

Intuition:
To invert a binary tree means to swap every node’s left and right child.
The simplest way to do this is recursion.
For each node, swap its children, then do the same for its left and right subtrees.

Approach:
- If the node is None → return None.
- Swap left and right children.
- Recursively invert the left subtree.
- Recursively invert the right subtree.
- Return the root.

Time Complexity:
- O(n), where n is the number of nodes (we visit each node once).

Space Complexity:
- O(h) for recursion stack, where h is the height of the tree.
  - O(log n) for balanced tree
  - O(n) for skewed tree
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()

        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):
    if not root:
        return []

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

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted1 = s.invertTree(root1)
    print(tree_to_list(inverted1))  # Expected: [4,7,2,9,6,3,1]

    # Example 2
    root2 = build_tree([2, 1, 3])
    inverted2 = s.invertTree(root2)
    print(tree_to_list(inverted2))  # Expected: [2,3,1]

    # Example 3
    root3 = build_tree([])
    inverted3 = s.invertTree(root3)
    print(tree_to_list(inverted3))  # Expected: []