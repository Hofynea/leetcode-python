"""
202. Happy Number
Category: Hashmap

Intuition:
Keep replacing `n` with sum of squares of its digits.
If we reach 1 → happy number.
If we enter a loop (number repeats) → not happy.

Approach:
- Use a set to remember seen numbers.
- If we reach 1 → return True.
- If we see the same number again → return False.

Time Complexity:
O(log n), because each step processes the digits of n, and the number shrinks quickly.

Space Complexity:
O(log n), for storing seen numbers.

Example:
Input: n = 19
Output: True
Explanation: 19 → 82 → 68 → 100 → 1 → happy number.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))   # Expected: True
    print(s.isHappy(2))    # Expected: False
    print(s.isHappy(1))    # Expected: True
    print(s.isHappy(116))  # Expected: False
