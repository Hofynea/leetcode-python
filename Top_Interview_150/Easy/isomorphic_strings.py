"""
205. Isomorphic Strings
Category: Hashmap

Intuition:
Check if each character in `s` consistently maps to one in `t`, and vice versa.

Approach:
- Use two hashmaps to track mappings in both directions.
- Loop through both strings.
- If a previous mapping conflicts with the current one, return False.
- Else, continue and return True.

Time Complexity:
- O(n), where n = len(s)

Space Complexity:
- O(1), only ASCII characters

Example:
Input: s = "egg", t = "add"
Output: True
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for sc, tc in zip(s, t):
            if sc in s_to_t and s_to_t[sc] != tc:
                return False
            if tc in t_to_s and t_to_s[tc] != sc:
                return False
            s_to_t[sc] = tc
            t_to_s[tc] = sc

        return True
