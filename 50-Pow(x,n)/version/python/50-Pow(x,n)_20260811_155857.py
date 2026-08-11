# Last updated: 11/08/2026, 15:58:57
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n < 0:
4            x = 1 / x
5            n = -n
6
7        if n == 0:
8            return 1
9
10        half = self.myPow(x, n // 2)
11
12        if n % 2 == 0:
13            return half * half
14        else:
15            return x * half * half