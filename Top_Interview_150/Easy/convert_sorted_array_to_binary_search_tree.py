from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_inorder(node):
    if not node:
        return []
    return print_inorder(node.left) + [node.val] + print_inorder(node.right)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)

if __name__ == "__main__":
    s = Solution()
    root1 = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    print("Inorder of BST for [-10, -3, 0, 5, 9]:", print_inorder(root1))

    root2 = s.sortedArrayToBST([1, 3])
    print("Inorder of BST for [1, 3]:", print_inorder(root2))
