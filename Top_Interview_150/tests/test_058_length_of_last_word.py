import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.length_of_last_word import Solution

class TestLengthOfLastWord(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().lengthOfLastWord("Hello World"), 5)

    def test_case_2(self):
        self.assertEqual(Solution().lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_case_3(self):
        self.assertEqual(Solution().lengthOfLastWord("luffy is still joyboy"), 6)

    def test_case_4(self):
        self.assertEqual(Solution().lengthOfLastWord("a"), 1)

    def test_case_5(self):
        self.assertEqual(Solution().lengthOfLastWord("Today is a good day   "), 3)

if __name__ == "__main__":
    unittest.main()
