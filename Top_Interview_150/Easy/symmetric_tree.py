"""
101. Symmetric Tree
Category: Binary Tree

Intuition:
We need to check if the tree is a mirror of itself.
That means the left subtree and right subtree must match in a mirrored way.

Approach:
- Use a helper function that checks if two subtrees are mirrors.
- Compare left of one with right of the other and vice versa.
- Recursively check all pairs of nodes.

Time Complexity:
- O(n), where n is the number of nodes in the tree (we visit each once).

Space Complexity:
- O(h) for recursion stack, where h is the height of the tree (O(log n) for balanced, O(n) for skewed).
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root.left, root.right)

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

if __name__ == "__main__":
    s = Solution()

    # Test case 1
    root1 = build_tree([1,2,2,3,4,4,3])
    print(s.isSymmetric(root1))  # Expected: True

    # Test case 2
    root2 = build_tree([1,2,2,None,3,None,3])
    print(s.isSymmetric(root2))  # Expected: False

    # Test case 3: single node
    root3 = build_tree([1])
    print(s.isSymmetric(root3))  # Expected: True

    # Test case 4: empty tree
    root4 = build_tree([])
    print(s.isSymmetric(root4))  # Expected: True