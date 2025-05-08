"""
169. Majority Element
Category: Array / String

Intuition:
The majority element appears more than ⌊n / 2⌋ times. So if we track a candidate and balance it against others,
the majority element will always survive. This is known as the Boyer-Moore Voting Algorithm.

Approach:
1. Initialize `count = 0` and `candidate = None`.
2. Loop through each number:
   - If count is 0, pick current number as candidate.
   - If current number is same as candidate, increment count.
   - Otherwise, decrement count.
3. Return the candidate.

Time Complexity:
- O(n): One pass through the array.

Space Complexity:
- O(1): Only two variables used.

Example:
Input:
    nums = [2, 2, 1, 1, 1, 2, 2]
Output:
    2
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = Solution().majorityElement(nums)
    print("Majority element:", result)  # Output: 2
