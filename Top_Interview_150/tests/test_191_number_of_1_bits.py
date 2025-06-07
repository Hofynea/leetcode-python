import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.number_of_1_bits import Solution

class TestNumberOf1Bits(unittest.TestCase):
    def test_case_1(self):
        n = 11
        self.assertEqual(Solution().hammingWeight(n), 3)

    def test_case_2(self):
        n = 128
        self.assertEqual(Solution().hammingWeight(n), 1)

    def test_case_3(self):
        n = 2147483645
        self.assertEqual(Solution().hammingWeight(n), 30)

if __name__ == "__main__":
    unittest.main()
    