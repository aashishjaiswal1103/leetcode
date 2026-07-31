# Last updated: 31/07/2026, 12:46:24
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        left = 1 
7        right = n 
8        result = n 
9        final = n
10        while left<=right:
11            mid = left+(right-left)//2
12            if isBadVersion(mid) is True :
13                result = mid 
14                right = mid -1 
15            else :
16                left = mid +1 
17            final = min(result , final)
18        return final 
19
20        