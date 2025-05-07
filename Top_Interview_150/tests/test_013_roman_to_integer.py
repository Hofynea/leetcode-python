import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.roman_to_integer import Solution

class TestRomanToInteger(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().romanToInt("III"), 3)

    def test_case_2(self):
        self.assertEqual(Solution().romanToInt("LVIII"), 58)

    def test_case_3(self):
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)

    def test_case_4(self):
        self.assertEqual(Solution().romanToInt("IX"), 9)

    def test_case_5(self):
        self.assertEqual(Solution().romanToInt("XL"), 40)

if __name__ == "__main__":
    unittest.main()
