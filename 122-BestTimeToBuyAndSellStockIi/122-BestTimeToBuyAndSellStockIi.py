# Last updated: 26/05/2026, 00:49:36
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        total = 0

        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1

            j = i

            while j < n - 1 and prices[j] < prices[j + 1]:
                j += 1

            total += prices[j] - prices[i]

            i = j + 1

        return total