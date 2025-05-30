"""
67. Add Binary
Category: Bit Manipulation

Intuition:
Add two binary strings from right to left, keeping track of carry.

Approach:
- Start from the end of both strings.
- Add corresponding bits + carry.
- Save result bit (sum % 2), update carry (sum // 2).
- Continue until both strings and carry are processed.
- Reverse result.

Time Complexity:
O(max(n, m)), where n and m are lengths of input strings.

Space Complexity:
O(max(n, m)), for the result string.

Example:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))       # Expected: "100"
    print(s.addBinary("1010", "1011"))  # Expected: "10101"
    print(s.addBinary("0", "0"))        # Expected: "0"
    print(s.addBinary("1", "111"))      # Expected: "1000"
    