"""
141. Linked List Cycle
Category: Linked List

Intuition:
We want to detect if the linked list has a cycle.
Use two pointers:
- A slow pointer moves one step at a time.
- A fast pointer moves two steps at a time.
If there is a cycle, fast will eventually meet slow.

Approach:
- Initialize two pointers: slow and fast.
- While fast and fast.next are not None:
    - Move slow one step.
    - Move fast two steps.
    - If slow == fast -> cycle detected -> return True.
- If loop ends, no cycle -> return False.

Time Complexity:
O(n), where n is the number of nodes.

Space Complexity:
O(1), constant space.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: True
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    # Example 1: [3,2,0,-4], pos = 1 -> cycle
    head1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle here
    print(Solution().hasCycle(head1))  # Expected: True

    # Example 2: [1,2], pos = 0 -> cycle
    head2 = ListNode(1)
    node2 = ListNode(2)
    head2.next = node2
    node2.next = head2  # cycle here
    print(Solution().hasCycle(head2))  # Expected: True

    # Example 3: [1], pos = -1 -> no cycle
    head3 = ListNode(1)
    head3.next = None
    print(Solution().hasCycle(head3))  # Expected: False

    # Example 4: empty list -> no cycle
    head4 = None
    print(Solution().hasCycle(head4))  # Expected: False
    