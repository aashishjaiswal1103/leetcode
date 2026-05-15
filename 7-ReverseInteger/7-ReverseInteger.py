# Last updated: 15/05/2026, 11:45:28
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            digit = x % 10 #take the last digit of x
            ans = ans * 10 + digit
            x //= 10
            if ans > 2**31 - 1 if sign == 1 else ans > 2**31:
                return 0

        return ans*sign