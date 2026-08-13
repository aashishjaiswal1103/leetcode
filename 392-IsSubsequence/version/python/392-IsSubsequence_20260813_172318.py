# Last updated: 13/08/2026, 17:23:18
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        a = len(s)
4        r = len(t)
5
6        def check(n, k):
7            if n == a:
8                return True
9            elif k == r:
10                return False
11            else:
12                if s[n] == t[k]:
13                    return check(n + 1, k + 1)
14                else:
15                    return check(n, k + 1)
16
17        return check(0, 0)
18