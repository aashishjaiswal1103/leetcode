# Last updated: 13/08/2026, 17:36:36
1class Solution:
2    def strStr(self, t: str, s: str) -> int:
3        a = len(s)
4        r = len(t)
5
6        def check(n, k):
7            if n == a:
8                return k - a
9
10            if k == r:
11                return -1
12
13            if s[n] == t[k]:
14                return check(n + 1, k + 1)
15
16            if n != 0:
17                return check(0, k - n + 1)
18
19            return check(0, k + 1)
20
21        return check(0, 0)