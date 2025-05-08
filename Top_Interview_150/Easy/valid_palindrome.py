"""
125. Valid Palindrome
Category: Two Pointers

Intuition:
Check if the string reads the same forward and backward, ignoring case and non-alphanumeric characters.

Approach:
- Use two pointers: one at the start, one at the end.
- Move each pointer inward, skipping non-alphanumeric characters.
- Compare lowercase characters. If any mismatch, return False.
- If all match, it's a palindrome.

Time Complexity:
- O(n): We visit each character once.

Space Complexity:
- O(1): No extra space used beyond pointers.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True
Explanation: After cleaning and lowering, we compare "amanaplanacanalpanama" with its reverse.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))  # True
    s = "race a car"
    print(Solution().isPalindrome(s))  # False
    s = " "
    print(Solution().isPalindrome(s))  # True
    s = "0P"
    print(Solution().isPalindrome(s))  # False
    s = "ab_a"
    print(Solution().isPalindrome(s))  # True
    