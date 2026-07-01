# Last updated: 01/07/2026, 23:28:57
# using dict
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        value = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,  "M": 1000 }
4
5        ans = 0
6        prev = 0
7
8        for ch in reversed(s):
9            curr = value[ch]
10
11            if curr < prev:
12                ans -= curr
13            else:
14                ans += curr
15
16            prev = curr
17
18        return ans