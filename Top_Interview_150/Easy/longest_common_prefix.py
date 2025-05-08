"""
14. Longest Common Prefix
Category: Array / String

Intuition:
Start with the first word as a candidate prefix.
Shorten it until all other words start with it.

Approach:
1. Take the first word as the prefix.
2. For each word in the list, reduce the prefix from the end
   until it matches the start of the word.
3. Return the resulting prefix.

Time Complexity:
- O(n * m): n = number of words, m = length of shortest word

Space Complexity:
- O(1): constant space

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print("Longest common prefix:", Solution().longestCommonPrefix(strs))  # Output: "fl"
    strs = ["dog", "racecar", "car"]
    print("Longest common prefix:", Solution().longestCommonPrefix(strs))  # Output: ""
    strs = ["a"]
    print("Longest common prefix:", Solution().longestCommonPrefix(strs))  # Output: "a"
    strs = ["ab", "a"]
    print("Longest common prefix:", Solution().longestCommonPrefix(strs))  # Output: "a"
