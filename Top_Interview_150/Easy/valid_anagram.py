"""
242. Valid Anagram
Category: Hashmap

Intuition:
If two strings use the same characters the same number of times,
they’re anagrams.

Approach:
- If lengths differ, return False.
- Use a counter (hashmap) to count character frequency in each string.
- Compare the counters.

Time Complexity:
- O(n), where n is the length of the strings.

Space Complexity:
- O(1), constant space since we only track lowercase English letters.

Example:
Input: s = "anagram", t = "nagaram"
Output: True
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))  # Output: False
print(solution.isAnagram("aacc", "ccac"))  # Output: False
print(solution.isAnagram("a", "ab"))  # Output: False
