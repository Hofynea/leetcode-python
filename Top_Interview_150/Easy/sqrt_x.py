"""
69. Sqrt(x)
Category: Math

Intuition:
To find the integer part of the square root of x, we can try numbers starting from 1 up to i * i > x.
But instead of checking linearly, we can use binary search to be efficient.

Approach:
- We perform binary search in the range [0, x].
- At each step, calculate mid = (left + right) // 2.
- If mid * mid == x, return mid.
- If mid * mid < x, store mid as the best guess and search right half.
- If mid * mid > x, search left half.
- Return the best guess when the loop ends.

Time Complexity:
- O(log x): Binary search on range [0, x].

Space Complexity:
- O(1): Constant space.

Example:
Input: x = 8
Output: 2
Explanation: The square root of 8 is about 2.82, so the integer part is 2.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    print(Solution().mySqrt(4))   # Output: 2
    print(Solution().mySqrt(8))   # Output: 2
    print(Solution().mySqrt(0))   # Output: 0
    print(Solution().mySqrt(1))   # Output: 1
    print(Solution().mySqrt(10))  # Output: 3
    print(Solution().mySqrt(16))  # Output: 4
    print(Solution().mySqrt(25))  # Output: 5
    print(Solution().mySqrt(36))  # Output: 6
    print(Solution().mySqrt(49))  # Output: 7
    print(Solution().mySqrt(64))  # Output: 8
    print(Solution().mySqrt(81))  # Output: 9
