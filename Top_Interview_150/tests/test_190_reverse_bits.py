import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.reverse_bits import Solution

class TestReverseBits(unittest.TestCase):
    def test_case_1(self):
        n = int("00000010100101000001111010011100", 2)
        expected = 964176192
        self.assertEqual(Solution().reverseBits(n), expected)

    def test_case_2(self):
        n = int("11111111111111111111111111111101", 2)
        expected = 3221225471
        self.assertEqual(Solution().reverseBits(n), expected)

    def test_case_3(self):
        n = int("00000000000000000000000000000000", 2)
        expected = 0
        self.assertEqual(Solution().reverseBits(n), expected)

    def test_case_4(self):
        n = int("11111111111111111111111111111111", 2)
        expected = 4294967295
        self.assertEqual(Solution().reverseBits(n), expected)

if __name__ == "__main__":
    unittest.main()
