# Last updated: 02/08/2026, 00:15:27
1class Solution:
2    def maxDistance(self, p: List[int], b: int) -> int:
3        ans = 0
4        low = 1
5
6        p.sort()
7        high = p[-1] - p[0]
8
9        while low <= high:
10            m = low + (high - low) // 2
11
12            c = 1
13            last = p[0]
14
15            for ch in p[1:]:
16                if ch - last >= m:
17                    c += 1
18                    last = ch
19
20            if c >= b:
21                ans = m
22                low = m + 1
23            else:
24                high = m - 1
25
26        return ans