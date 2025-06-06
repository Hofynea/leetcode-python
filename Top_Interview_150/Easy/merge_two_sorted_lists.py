"""
21. Merge Two Sorted Lists
Category: Linked List

Intuition:
We need to merge two sorted linked lists into one sorted list.
Use a dummy node and build the merged list step by step by always choosing the smaller node.

Approach:
- Create a dummy node and a pointer current.
- While both list1 and list2 are not empty:
    - Compare list1.val and list2.val.
    - Attach the smaller node to current.next.
    - Move current and the list we used.
- After the loop, attach the remaining part of list1 or list2.
- Return dummy.next (head of the merged list).

Time Complexity:
O(n + m), where n and m are the lengths of the two lists.

Space Complexity:
O(1), we merge in-place using existing nodes.

Example:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


if __name__ == "__main__":
    # Example 1
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    def print_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print(result)

    result = Solution().mergeTwoLists(l1, l2)
    print_list(result)  # Expected: [1, 1, 2, 3, 4, 4]

    # Example 2
    result = Solution().mergeTwoLists(None, None)
    print_list(result)  # Expected: []

    # Example 3
    l3 = None
    l4 = ListNode(0)
    result = Solution().mergeTwoLists(l3, l4)
    print_list(result)  # Expected: [0]
    