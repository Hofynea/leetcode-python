"""
219. Contains Duplicate II
Category: Hashmap

Intuition:
Use a hashmap to store the last index of each number.
If we see the same number again, check if the distance is <= k.

Approach:
- Loop through nums with index i.
- If nums[i] is in hashmap:
    - If i - last_index <= k → return True.
- Update hashmap with current index.

Time Complexity:
O(n), where n is length of nums.

Space Complexity:
O(n), for the hashmap.

Example:
Input: nums = [1, 0, 1, 1], k = 1
Output: True
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}

        for i, num in enumerate(nums):
            if num in num_to_index:
                if i - num_to_index[num] <= k:
                    return True
            num_to_index[num] = i

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))   # Expected: True
    print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))   # Expected: True
    print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Expected: False
    