import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Easy.best_time_to_buy_and_sell_stock import Solution

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_case_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(Solution().maxProfit(prices), 5)

    def test_case_2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(Solution().maxProfit(prices), 0)

    def test_case_3(self):
        prices = [1, 2]
        self.assertEqual(Solution().maxProfit(prices), 1)

    def test_case_4(self):
        prices = [2, 4, 1]
        self.assertEqual(Solution().maxProfit(prices), 2)

    def test_case_5(self):
        prices = [3, 2, 6, 5, 0, 3]
        self.assertEqual(Solution().maxProfit(prices), 4)

if __name__ == "__main__":
    unittest.main()
    