"""
9. Palindrome Number
Category: Math

Intuition:
A number is a palindrome if it reads the same forward and backward.
The easiest way is to convert the number to a string and compare it to its reverse.

Approach:
- If x is negative, it cannot be a palindrome -> return False.
- Convert x to a string.
- Compare the string with its reverse.
- If equal -> return True.
- Else -> return False.

Time Complexity:
O(n), where n is the number of digits in x.

Space Complexity:
O(n), for the string conversion.

Example:
Input: 121
Output: True
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))    # Expected: True
    print(s.isPalindrome(-121))   # Expected: False
    print(s.isPalindrome(10))     # Expected: False
    print(s.isPalindrome(0))      # Expected: True
    print(s.isPalindrome(12321))  # Expected: True
    