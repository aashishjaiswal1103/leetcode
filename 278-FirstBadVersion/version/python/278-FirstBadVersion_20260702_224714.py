# Last updated: 02/07/2026, 22:47:14
# using binary search
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        left, right = 1, n
7
8        while left < right:
9            mid = (left + right) // 2
10
11            if isBadVersion(mid):
12                right = mid
13            else:
14                left = mid + 1
15
16        return left