import unittest
from collections import deque
from typing import Optional
from Easy.average_of_levels_in_binary_tree import Solution, TreeNode

def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root

class TestAverageOfLevels(unittest.TestCase):
    def test_case_1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        expected = [3.0, 14.5, 11.0]
        result = Solution().averageOfLevels(root)
        self.assertEqual(result, expected)

    def test_case_2(self):
        root = build_tree([5, 1, 4, None, None, 3, 6])
        expected = [5.0, 2.5, 4.5]
        result = Solution().averageOfLevels(root)
        self.assertEqual(result, expected)

    def test_case_3(self):
        root = build_tree([10])
        expected = [10.0]
        result = Solution().averageOfLevels(root)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()