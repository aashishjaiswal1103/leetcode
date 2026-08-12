# Last updated: 12/08/2026, 20:54:04
1class Solution:
2    def fib(self, n: int) -> int:
3        if n <= 1:
4            return n
5        return self.fib(n - 1) + self.fib(n - 2)