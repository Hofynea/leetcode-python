"""
88. Merge Sorted Array

Intuition:
We need to merge two sorted arrays into one sorted array. Instead of creating a new array,
we can modify `nums1` in-place, leveraging its extra space. Starting from the end allows us
to place larger elements first without overwriting any useful data.

Approach:
1. Initialize pointers:
   - `p1` = m - 1 (end of valid elements in nums1)
   - `p2` = n - 1 (end of nums2)
   - `p` = m + n - 1 (end of nums1’s allocated space)

2. Compare and merge from the back:
   - If `nums1[p1] > nums2[p2]`: put `nums1[p1]` at `nums1[p]`, move `p1--`, `p--`
   - Else: put `nums2[p2]` at `nums1[p]`, move `p2--`, `p--`

3. Copy remaining `nums2` values (if any) into `nums1`.

Time Complexity:
- O(m + n): We traverse each element from the back once.
- O(1): In-place merge, constant extra space.

Example:
Input:
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

Output:
    [1, 2, 2, 3, 5, 6]
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

    Solution().merge(nums1, m, nums2, n)
    print("Merged array:", nums1)  # Output: [1, 2, 2, 3, 5, 6]
    