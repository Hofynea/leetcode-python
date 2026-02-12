"""
112. Path Sum
Category: Binary Tree DFS

Intuition:
We need to check if there's a root-to-leaf path that adds up to a given target sum.
If we reach a leaf and the sum along the path equals the target, return True.

Approach:
- Use Depth-First Search (DFS) recursively.
- Subtract each node’s value from the targetSum as we go deeper.
- If we hit a leaf node, check if the remaining sum equals the node’s value.

Time Complexity:
- O(n), where n is the number of nodes in the tree.

Space Complexity:
- O(h), where h is the height of the tree (due to recursion stack).
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # If we're at a leaf node
        if not root.left and not root.right:
            return targetSum == root.val

        # Recurse on left and right with updated target
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

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
    root1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(s.hasPathSum(root1, 22))  # Output: True

    root2 = build_tree([1,2,3])
    print(s.hasPathSum(root2, 5))  # Output: False

    root3 = build_tree([])
    print(s.hasPathSum(root3, 0))  # Output: False