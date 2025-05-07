"""
27. Remove Element

Intuition:
We need to remove all instances of a specific value from the list in-place. Since the order 
of elements doesn't matter, we can use a two-pointer technique to overwrite unwanted values.

Approach:
1. Initialize a pointer `k` to track where the next non-`val` element should be placed.
2. Iterate through the array.
   - If the current value is not equal to `val`, assign it to index `k` and increment `k`.
3. Return `k`, which represents the new length of the modified array.

Time Complexity:
- O(n): We visit each element once.

Space Complexity:
- O(1): In-place operation, no additional memory used.

Example:
Input:
    nums = [3, 2, 2, 3], val = 3
Output:
    k = 2, nums = [2, 2, _, _] (underscores can be anything)
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    k = Solution().removeElement(nums, val)
    print("Length after removal:", k)
    print("Modified array:", nums[:k])  # Output: [2, 2]
    