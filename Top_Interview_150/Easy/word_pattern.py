"""
290. Word Pattern
Category: Hashmap

Intuition:
We want to make sure each letter in the pattern maps to one unique word in the string,
and each word maps to one unique letter — like a perfect one-to-one match.

Approach:
- Split the input string `s` into words.
- If the number of pattern letters and words don’t match, return False.
- Use two hashmaps:
    - One to track letter → word
    - One to track word → letter
- Loop through both at the same time and make sure the mapping is consistent.
- If it ever mismatches, return False.
- If the whole loop completes, return True.

Time Complexity:
- O(n), where n = length of pattern / number of words.

Space Complexity:
- O(n), for the mappings.

Example:
Input: pattern = "abba", s = "dog cat cat dog"
Output: True
Explanation: 
  a → dog, b → cat. Both mappings stay consistent and complete.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))    # True
    print(s.wordPattern("abba", "dog cat cat fish"))   # False
    print(s.wordPattern("aaaa", "dog cat cat dog"))    # False
    print(s.wordPattern("abc", "dog cat fish"))        # True
    print(s.wordPattern("abc", "dog dog dog"))         # False
