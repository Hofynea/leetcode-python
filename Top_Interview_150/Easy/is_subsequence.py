"""
392. Is Subsequence
Category: Two Pointers

Intuition:
We want to check if all characters of `s` appear in `t` in the same order.
So we walk through both strings, moving forward only when characters match.

Approach:
- Use two pointers: one for `s`, one for `t`.
- Loop through `t`, and whenever characters match, move the `s` pointer.
- If we go through all of `s`, it's a subsequence.

Time Complexity:
- O(n): We go through string `t` once, comparing characters.

Space Complexity:
- O(1): No extra data structures used.

Example:
Input: s = "abc", t = "ahbgdc"
Output: True
Explanation: a → h → b → g → d → c — all characters found in order.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == "__main__":
    print(Solution().isSubsequence("abc", "ahbgdc"))  # True
    print(Solution().isSubsequence("axc", "ahbgdc"))  # False
    print(Solution().isSubsequence("", "ahbgdc"))     # True
    print(Solution().isSubsequence("abc", ""))        # False
    