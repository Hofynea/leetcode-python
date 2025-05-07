"""
121. Best Time to Buy and Sell Stock

Intuition:
To maximize profit, we want to buy at the lowest price before selling at the highest price.
By scanning prices from left to right, we can keep track of the lowest price seen so far.

Approach:
1. Initialize `min_price` to infinity and `max_profit` to 0.
2. Iterate over the prices:
   - If current price < `min_price`, update `min_price`.
   - Otherwise, calculate potential profit and update `max_profit` if it’s higher.
3. Return `max_profit`.

Time Complexity:
- O(n): Single pass through the list.

Space Complexity:
- O(1): No additional space used.

Example:
Input:
    prices = [7, 1, 5, 3, 6, 4]
Output:
    5  (Buy at 1, sell at 6)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Max profit:", Solution().maxProfit(prices))  # Output: 5
    prices = [7, 6, 4, 3, 1]
    print("Max profit:", Solution().maxProfit(prices))  # Output: 0
    