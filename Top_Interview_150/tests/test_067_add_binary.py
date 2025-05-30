import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.add_binary import Solution

class TestAddBinary(unittest.TestCase):
    def test_case_1(self):
        a = "11"
        b = "1"
        self.assertEqual(Solution().addBinary(a, b), "100")

    def test_case_2(self):
        a = "1010"
        b = "1011"
        self.assertEqual(Solution().addBinary(a, b), "10101")

    def test_case_3(self):
        a = "0"
        b = "0"
        self.assertEqual(Solution().addBinary(a, b), "0")

    def test_case_4(self):
        a = "1"
        b = "111"
        self.assertEqual(Solution().addBinary(a, b), "1000")

if __name__ == "__main__":
    unittest.main()
    