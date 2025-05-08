"""
13. Roman to Integer
Category: Array / String

Intuition:
Roman numerals are normally added together from left to right.
But if a smaller value comes before a larger one (like IV), we subtract instead of add.

Approach:
1. Create a dictionary that maps each Roman letter to its integer value.
2. Loop through the string from right to left.
3. If the current value is less than the previous one, subtract it.
4. Otherwise, add it to the total.
5. Return the total.

Time Complexity:
- O(n): We check each character once.

Space Complexity:
- O(1): Just a few variables and a fixed dictionary.

Example:
Input:  "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4 → total = 1994
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        for c in reversed(s):
            curr = roman[c]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr

        return total


if __name__ == "__main__":
    s = "MCMXCIV"
    print("Integer value:", Solution().romanToInt(s))  # Output: 1994
   