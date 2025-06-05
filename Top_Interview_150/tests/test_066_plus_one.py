import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.plus_one import Solution

class TestPlusOne(unittest.TestCase):
    def test_case_1(self):
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        self.assertEqual(Solution().plusOne(digits), expected)

    def test_case_2(self):
        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        self.assertEqual(Solution().plusOne(digits), expected)

    def test_case_3(self):
        digits = [9]
        expected = [1, 0]
        self.assertEqual(Solution().plusOne(digits), expected)

    def test_case_4(self):
        digits = [9, 9, 9]
        expected = [1, 0, 0, 0]
        self.assertEqual(Solution().plusOne(digits), expected)

    def test_case_5(self):
        digits = [0]
        expected = [1]
        self.assertEqual(Solution().plusOne(digits), expected)

if __name__ == "__main__":
    unittest.main()
    