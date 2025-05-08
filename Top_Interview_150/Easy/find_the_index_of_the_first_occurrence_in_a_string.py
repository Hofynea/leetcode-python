"""
28. Find the Index of the First Occurrence in a String

Intuition:
We need to find where the needle string starts inside the haystack string.
Python has a built-in function that does exactly that: .find()

Approach:
- Use haystack.find(needle) to get the index of the first match.
- If needle is not found, it returns -1.

Time Complexity:
- O(n * m) worst-case, depending on implementation

Space Complexity:
- O(1)

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    print(Solution().strStr("sadbutsad", "sad"))    # Output: 0
    print(Solution().strStr("leetcode", "leeto"))   # Output: -1
    print(Solution().strStr("hello", "ll"))         # Output: 2
    print(Solution().strStr("aaaaa", "bba"))        # Output: -1
    