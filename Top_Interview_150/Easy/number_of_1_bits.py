"""
191. Number of 1 Bits
Category: Bit Manipulation

Intuition:
We want to count how many '1' bits are in the binary representation of n.

Approach:
- Initialize count = 0.
- While n is not zero:
    - Do n & (n - 1) to turn off the lowest '1' bit.
    - Increment count.
- Return count.

Time Complexity:
O(1), because n is a 32-bit integer → max 32 iterations.

Space Complexity:
O(1), constant space.

Example:
Input: n = 11
Output: 3
Explanation: 11 in binary is 1011 → three 1's.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(11))         # Expected: 3
    print(s.hammingWeight(128))        # Expected: 1
    print(s.hammingWeight(2147483645)) # Expected: 30
    