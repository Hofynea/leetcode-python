"""
228. Summary Ranges
Category: Intervals

Intuition:
Go from left to right, group consecutive numbers into ranges.

Approach:
- Start a new range with first number.
- If current number is not consecutive, save previous range.
- After loop, save the last range.

Time Complexity:
O(n), because we visit each number once.

Space Complexity:
O(n), to store result.

Example:
Input: [0, 1, 2, 4, 5, 7]
Output: ["0->2", "4->5", "7"]
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))        # Expected: ["0->2","4->5","7"]
    print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))     # Expected: ["0", "2->4", "6", "8->9"]
    print(s.summaryRanges([]))                        # Expected: []
    print(s.summaryRanges([5]))                       # Expected: ["5"]
    