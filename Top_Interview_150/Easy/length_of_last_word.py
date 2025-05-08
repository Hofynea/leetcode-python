"""
58. Length of Last Word

Intuition:
We need the length of the last word in a string. The string may have extra spaces.
We can trim the ends, split the string into words, and measure the last one.

Approach:
1. Use strip() to remove extra spaces from both ends.
2. Split the string into a list of words.
3. Return the length of the last word.

Time Complexity:
- O(n): We scan the string once.

Space Complexity:
- O(n): The split creates a list of words.

Example:
Input: "Hello World"
Output: 5  (Last word is "World")
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


if __name__ == "__main__":
    s = "Hello World"
    print("Length of last word:", Solution().lengthOfLastWord(s))  # Output: 5

    s = "   fly me   to   the moon  "
    print("Length of last word:", Solution().lengthOfLastWord(s))  # Output: 4

    s = "luffy is still joyboy"
    print("Length of last word:", Solution().lengthOfLastWord(s))  # Output: 6
