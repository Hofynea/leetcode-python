"""
35. Search Insert Position
Category: Binary Search

Intuition:
Use binary search to find the index of the target.
If not found, return the index where it would be inserted.

Approach:
- Initialize left = 0, right = len(nums) - 1.
- While left <= right:
    - mid = (left + right) // 2
    - If nums[mid] == target -> return mid.
    - If nums[mid] < target -> search right half.
    - Else -> search left half.
- Return left as the insert position.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Example:
Input: nums = [1,3,5,6], target = 2
Output: 1
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))  # Expected: 2
    print(s.searchInsert([1, 3, 5, 6], 2))  # Expected: 1
    print(s.searchInsert([1, 3, 5, 6], 7))  # Expected: 4
    