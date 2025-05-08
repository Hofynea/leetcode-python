import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.climbing_stairs import Solution

class TestClimbingStairs(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_case_2(self):
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_case_3(self):
        self.assertEqual(Solution().climbStairs(4), 5)

    def test_case_4(self):
        self.assertEqual(Solution().climbStairs(5), 8)

    def test_case_5(self):
        self.assertEqual(Solution().climbStairs(6), 13)

    def test_case_6(self):
        self.assertEqual(Solution().climbStairs(7), 21)

    def test_case_7(self):
        self.assertEqual(Solution().climbStairs(8), 34)

    def test_case_8(self):
        self.assertEqual(Solution().climbStairs(9), 55)

if __name__ == "__main__":
    unittest.main()
