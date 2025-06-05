"""
66. Plus One
Category: Math

Intuition:
We need to add one to the integer represented by the digits array.
Start from the last digit:
- If the digit is less than 9 -> add one and return.
- If the digit is 9 -> set it to 0 and continue (carry over).
If all digits are 9 -> we need to insert 1 at the front.

Approach:
- Loop through digits from right to left.
- If current digit is less than 9:
    - Add one, return the array.
- If current digit is 9:
    - Set to 0 and continue.
- If loop completes, all were 9 -> insert 1 at the front.

Time Complexity:
O(n), where n is the number of digits.

Space Complexity:
O(1), in-place modification (ignoring result array return).

Example:
Input: [1, 2, 3]
Output: [1, 2, 4]
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))    # Expected: [1, 2, 4]
    print(s.plusOne([4, 3, 2, 1])) # Expected: [4, 3, 2, 2]
    print(s.plusOne([9]))          # Expected: [1, 0]
    print(s.plusOne([9, 9, 9]))    # Expected: [1, 0, 0, 0]
    print(s.plusOne([0]))          # Expected: [1]
