# Last updated: 15/05/2026, 11:45:12
class Solution:
    def fib(self, n: int) -> int:
        if (n ==0 or n == 1):
            return n 
        return self.fib(n-1)+self.fib(n-2)
        