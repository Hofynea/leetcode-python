"""
26. Remove Duplicates from Sorted Array

Intuition:
The array is sorted in non-decreasing order, so duplicates are grouped together.
We can iterate through the array, comparing each element with the one before it.
If it's a new unique element, we write it at index `k`.

Approach:
1. Use a pointer `k = 1` to track where to place the next unique element.
2. Loop from index 1 to end of array.
   - If current element is different from previous, store it at `nums[k]`, then increment `k`.
3. Return `k`, the count of unique elements.

Time Complexity:
- O(n): Traverse each element once.

Space Complexity:
- O(1): Constant space, in-place operation.

Example:
Input:
    nums = [1, 1, 2]
Output:
    k = 2, nums = [1, 2, ...]
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # Pointer for the position of the next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    nums = [1, 1, 2]
    k = Solution().removeDuplicates(nums)
    print("Length after deduplication:", k)
    print("Modified array:", nums[:k])  # Output: [1, 2]
    