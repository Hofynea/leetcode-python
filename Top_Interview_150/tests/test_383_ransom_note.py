import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.ransom_note import Solution

class TestRansomNote(unittest.TestCase):
    def test_case_1(self):
        ransomNote = "a"
        magazine = "b"
        self.assertFalse(Solution().canConstruct(ransomNote, magazine))

    def test_case_2(self):
        ransomNote = "aa"
        magazine = "ab"
        self.assertFalse(Solution().canConstruct(ransomNote, magazine))

    def test_case_3(self):
        ransomNote = "aa"
        magazine = "aab"
        self.assertTrue(Solution().canConstruct(ransomNote, magazine))

    def test_case_4(self):
        ransomNote = ""
        magazine = "abc"
        self.assertTrue(Solution().canConstruct(ransomNote, magazine))

    def test_case_5(self):
        ransomNote = "abc"
        magazine = "abc"
        self.assertTrue(Solution().canConstruct(ransomNote, magazine))

    def test_case_6(self):
        ransomNote = "abc"
        magazine = "aabbcc"
        self.assertTrue(Solution().canConstruct(ransomNote, magazine))

    def test_case_7(self):
        ransomNote = "aabbcc"
        magazine = "abc"
        self.assertFalse(Solution().canConstruct(ransomNote, magazine))

    def test_case_8(self):
        ransomNote = "aaaa"
        magazine = "aaa"
        self.assertFalse(Solution().canConstruct(ransomNote, magazine))

    def test_case_9(self):
        ransomNote = "xyz"
        magazine = "xyzz"
        self.assertTrue(Solution().canConstruct(ransomNote, magazine))

    def test_case_10(self):
        ransomNote = "xyz"
        magazine = "xxyyzz"
        self.assertTrue(Solution().canConstruct(ransomNote, magazine))

if __name__ == "__main__":
    unittest.main()
    