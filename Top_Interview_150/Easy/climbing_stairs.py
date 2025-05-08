"""
70. Climbing Stairs
Category: 1D Dynamic Programming

Intuition:
This is a classic Fibonacci-like problem.
To reach the nth stair, you can come from either the (n-1)th or the (n-2)th stair.
So, the total number of ways to reach n is:
ways(n) = ways(n-1) + ways(n-2)

Approach:
- Handle small n (1 or 2) as base cases directly: return n.
- Use two variables:
    • first → stores number of ways to reach stair n−2
    • second → stores number of ways to reach stair n−1
- For each step from 3 to n, compute the new number of ways: first + second
- Shift the window: update first and second for the next step.
- Finally, return second, which holds the answer for n.

Time Complexity:
- O(n): We loop from 3 to n.

Space Complexity:
- O(1): Only two variables are used, no array.

Example:
Input: n = 3
Output: 3
Explanation: [1+1+1], [1+2], [2+1]
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second


if __name__ == "__main__":
    print(Solution().climbStairs(2))  # Output: 2
    print(Solution().climbStairs(3))  # Output: 3
    print(Solution().climbStairs(4))  # Output: 5
    print(Solution().climbStairs(5))  # Output: 8
    print(Solution().climbStairs(6))  # Output: 13
    print(Solution().climbStairs(7))  # Output: 21
    print(Solution().climbStairs(8))  # Output: 34
    print(Solution().climbStairs(9))  # Output: 55
    