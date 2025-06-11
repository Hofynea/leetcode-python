"""
136. Single Number
Category: Bit Manipulation

Intuition:
- Every number appears twice except one.
- Use XOR: a ^ a = 0, a ^ 0 = a
- XOR all numbers → pairs cancel out → result is the single number.

Approach:
- Initialize result = 0
- XOR all elements in nums
- Return result

Time Complexity:
O(n), where n is length of nums

Space Complexity:
O(1), constant space

Example:
Input: [4,1,2,1,2]
Output: 4
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))        # Expected: 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # Expected: 4
    print(s.singleNumber([1]))             # Expected: 1
