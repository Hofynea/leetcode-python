"""
20. Valid Parentheses
Category: Stack

Intuition:
- Use a stack to track open parentheses.
- If we see an opening bracket -> push to stack.
- If we see a closing bracket -> pop from stack and check if it matches.
- At the end:
    - If stack is empty -> valid.
    - If stack is not empty -> invalid.

Approach:
- Create an empty stack.
- Create a mapping of closing → opening brackets: {')': '(', '}': '{', ']': '['}
- For each character c in string s:
    - If c is an opening → push to stack.
    - If c is a closing:
        - If stack is empty or top of stack doesn't match -> return False.
        - Otherwise, pop from stack.
- After loop, return True if stack is empty, False otherwise.

Time Complexity:
O(n), where n is the length of s.

Space Complexity:
O(n), for the stack.

Example:
Input: "()[]{}"
Output: True
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()

        return not stack


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))           # Expected: True
    print(s.isValid("()[]{}"))       # Expected: True
    print(s.isValid("(]"))           # Expected: False
    print(s.isValid("([{}])"))       # Expected: True
    print(s.isValid("((("))          # Expected: False
