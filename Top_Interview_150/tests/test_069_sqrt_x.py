import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.sqrt_x import Solution

class TestSqrtX(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().mySqrt(4), 2)

    def test_case_2(self):
        self.assertEqual(Solution().mySqrt(8), 2)

    def test_case_3(self):
        self.assertEqual(Solution().mySqrt(0), 0)

    def test_case_4(self):
        self.assertEqual(Solution().mySqrt(1), 1)

    def test_case_5(self):
        self.assertEqual(Solution().mySqrt(10), 3)

    def test_case_6(self):
        self.assertEqual(Solution().mySqrt(2147395599), 46339)

if __name__ == "__main__":
    unittest.main()
