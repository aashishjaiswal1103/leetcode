# Last updated: 01/08/2026, 12:12:24
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        low = 1
4        high = max(piles)
5        ans = 0 
6        while  low <= high:
7            k = low +(high - low)//2
8            hours = 0 
9            for p in piles:
10                hours += (p+k-1)//k 
11            if hours <= h :
12                ans = k 
13                high = k-1
14            else:
15                 low = k+1   
16        return ans     
17
18
19
20        