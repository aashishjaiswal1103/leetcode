# Last updated: 22/06/2026, 23:51:15
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        n = len(haystack)
4        m = len(needle)
5
6        for i in range(n - m + 1):
7            if haystack[i:i+m] == needle:
8                return i
9
10        return -1