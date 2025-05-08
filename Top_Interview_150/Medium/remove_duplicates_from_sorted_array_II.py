"""
80. Remove Duplicates from Sorted Array II

Intuition:
Since the array is sorted, duplicates are together. We can keep at most 2 of each number.
If the current number is different from the one 2 spots before, it’s safe to keep.

Approach:
1. If the array has 2 or fewer items, return the length.
2. Use two pointers:
   - `i` scans the array.
   - `k` tracks where to write the next valid number.
3. If nums[i] != nums[k - 2], keep it and move `k`.

Time Complexity:
- O(n): Single pass through the array

Space Complexity:
- O(1): In-place modification

Example:
Input:  [1,1,1,2,2,3]
Output: [1,1,2,2,3] → length = 5
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = Solution().removeDuplicates(nums)
    print("After removal:", nums[:k])  # Output: [1, 1, 2, 2, 3]

    nums = [0,0,1,1,1,1,2,3,3]
    k = Solution().removeDuplicates(nums)
    print("After removal:", nums[:k])  # Output: [0, 0, 1, 1, 2, 3, 3]

    nums = [1,1,1,2,2,2,3,3]
    k = Solution().removeDuplicates(nums)
    print("After removal:", nums[:k])  # Output: [1, 1, 2, 2, 3, 3]

