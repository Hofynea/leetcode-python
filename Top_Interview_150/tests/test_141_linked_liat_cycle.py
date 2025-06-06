

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.linked_list_cycle import Solution, ListNode

class TestLinkedListCycle(unittest.TestCase):
    def test_case_1(self):
        head = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # cycle
        self.assertTrue(Solution().hasCycle(head))

    def test_case_2(self):
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node2.next = head  # cycle
        self.assertTrue(Solution().hasCycle(head))

    def test_case_3(self):
        head = ListNode(1)
        head.next = None
        self.assertFalse(Solution().hasCycle(head))

    def test_case_4(self):
        head = None
        self.assertFalse(Solution().hasCycle(head))

if __name__ == "__main__":
    unittest.main()
    