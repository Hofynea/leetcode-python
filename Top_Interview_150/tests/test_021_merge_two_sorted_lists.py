import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.merge_two_sorted_lists import Solution, ListNode

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestMergeTwoSortedLists(unittest.TestCase):
    def test_case_1(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        result = Solution().mergeTwoLists(l1, l2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_case_2(self):
        result = Solution().mergeTwoLists(None, None)
        self.assertEqual(linked_list_to_list(result), [])

    def test_case_3(self):
        l3 = None
        l4 = ListNode(0)

        result = Solution().mergeTwoLists(l3, l4)
        self.assertEqual(linked_list_to_list(result), [0])

if __name__ == "__main__":
    unittest.main()
    