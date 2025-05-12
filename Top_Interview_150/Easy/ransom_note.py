"""
383. Ransom Note
Category: Hashmap

Intuition:
We just need to check if the magazine has enough of each letter needed to build the ransom note.

Approach:
- Count the letters in the magazine using a hashmap.
- Go through each letter in the ransom note.
- If a letter is missing or used up, return False.
- If all letters are found in sufficient quantity, return True.

Time Complexity:
- O(n + m), where n is the length of ransomNote and m is the length of magazine.

Space Complexity:
- O(1), only 26 lowercase letters.

Example:
Input: ransomNote = "aa", magazine = "aab"
Output: True
Explanation: Magazine has enough a's to build the ransom note.
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        
        for char in ransomNote:
            if mag_count[char] == 0:
                return False
            mag_count[char] -= 1
        
        return True
    