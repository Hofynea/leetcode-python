"""
1. Two Sum
Category: Hashmap

Intuition:
For each number, we want to know if we've already seen another number
that would add up with it to reach the target.
We can use a hashmap to remember numbers we've seen so far.

Approach:
- Create a hashmap to store number → index.
- Loop through nums:
    - For each num, calculate needed = target - num.
    - If needed is in hashmap → return its index and current index.
    - Else, store current num in hashmap.

Time Complexity:
- O(n), where n is the length of nums.

Space Complexity:
- O(n), for the hashmap.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in num_to_index:
                return [num_to_index[needed], i]
            num_to_index[num] = i

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))    # Expected: [0, 1]
    print(s.twoSum([3, 2, 4], 6))         # Expected: [1, 2]
    print(s.twoSum([3, 3], 6))            # Expected: [0, 1]
    print(s.twoSum([1, 5, 3, 7], 10))     # Expected: [2, 3]
    print(s.twoSum([1, 2, 3, 4, 5], 9))   # Expected: [3, 4]
    