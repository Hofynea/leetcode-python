import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Hard.candy import Solution

class TestCandy(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().candy([1, 0, 2]), 5)

    def test_case_2(self):
        self.assertEqual(Solution().candy([1, 2, 2]), 4)

    def test_case_3(self):
        self.assertEqual(Solution().candy([1, 3, 2, 2, 1]), 7)

    def test_case_4(self):
        self.assertEqual(Solution().candy([1, 2, 87, 87, 87, 2, 1]), 13)

    def test_case_5(self):
        self.assertEqual(Solution().candy([1, 2, 3, 4, 5]), 15)

if __name__ == "__main__":
    unittest.main()
