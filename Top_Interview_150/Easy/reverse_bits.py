"""
190. Reverse Bits
Category: Bit Manipulation

Intuition:
We are given a 32-bit unsigned integer `n`.
We want to reverse its bits — that is, the least significant bit becomes the most significant, and so on.

The easiest way is to process one bit at a time:
- Extract the last bit of `n`.
- Append it to the result.
- Shift `n` to the right, shift result to the left.

Approach:
- Initialize result = 0.
- Loop 32 times:
    - Shift result left by 1 to make space.
    - Add the last bit of n (n & 1) to result.
    - Shift n right by 1 to process the next bit.
- At the end, return result masked with 0xFFFFFFFF to ensure 32 bits.

Time Complexity:
O(1), because we always do 32 iterations.

Space Complexity:
O(1), constant space.

Example:
Input: n = 43261596
(binary: 00000010100101000001111010011100)
Output: 964176192
(binary: 00111001011110000010100101000000)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res & 0xFFFFFFFF


if __name__ == "__main__":
    s = Solution()
    n1 = int("00000010100101000001111010011100", 2)
    n2 = int("11111111111111111111111111111101", 2)

    print(s.reverseBits(n1))  # Expected: 964176192
    print(s.reverseBits(n2))  # Expected: 3221225471
