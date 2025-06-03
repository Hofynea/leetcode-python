import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.valid_parentheses import Solution

class TestValidParentheses(unittest.TestCase):
    def test_case_1(self):
        s = "()"
        self.assertTrue(Solution().isValid(s))

    def test_case_2(self):
        s = "()[]{}"
        self.assertTrue(Solution().isValid(s))

    def test_case_3(self):
        s = "(]"
        self.assertFalse(Solution().isValid(s))

    def test_case_4(self):
        s = "([{}])"
        self.assertTrue(Solution().isValid(s))

    def test_case_5(self):
        s = "((("
        self.assertFalse(Solution().isValid(s))

if __name__ == "__main__":
    unittest.main()
    