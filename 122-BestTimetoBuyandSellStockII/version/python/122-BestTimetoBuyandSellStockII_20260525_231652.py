# Last updated: 25/05/2026, 23:16:52
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        i = 0
5        total = 0
6
7        while i < n - 1:
8            while i < n - 1 and prices[i] >= prices[i + 1]:
9                i += 1
10
11            j = i
12
13            while j < n - 1 and prices[j] < prices[j + 1]:
14                j += 1
15
16            total += prices[j] - prices[i]
17
18            i = j + 1
19
20        return total