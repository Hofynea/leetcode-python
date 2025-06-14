"""
637. Average of Levels in Binary Tree
Category: Binary Tree BFS

Intuition:
We need to compute the average value of each level in a binary tree.
The simplest way to do this is to use Breadth-First Search (BFS):
traverse the tree level by level using a queue.

Approach:
- Use a queue to perform BFS.
- For each level:
    - Sum all node values.
    - Divide by the number of nodes in that level.
- Append the result to an output list.

Time Complexity:
- O(n), where n is the number of nodes in the tree.

Space Complexity:
- O(m), where m is the maximum number of nodes at any level (queue size).

Example:
Input: [3,9,20,null,null,15,7]
Output: [3.0, 14.5, 11.0]
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result

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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(s.averageOfLevels(root1))  # Output: [3.0, 14.5, 11.0]

    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print(s.averageOfLevels(root2))  # Output: [5.0, 2.5, 4.5]