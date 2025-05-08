"""
135. Candy

Intuition:
We need to give out the minimum number of candies so:
1. Every child gets at least one.
2. Children with higher ratings than neighbors get more candies.

Approach:
1. Give everyone 1 candy.
2. Left to right pass — if current rating is higher than left neighbor, increase candy count.
3. Right to left pass — do the same but take the max between current and right neighbor + 1.

Time Complexity:
- O(n): Two passes through the array

Space Complexity:
- O(n): For the candies array

Example:
Input: [1,0,2]
Output: 5  → [2,1,2]
"""

class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    print(Solution().candy([1, 0, 2]))  # Output: 5
    print(Solution().candy([1, 2, 2]))  # Output: 4
    print(Solution().candy([1, 3, 2, 2, 1]))  # Output: 7
    print(Solution().candy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 55
    