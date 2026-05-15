# Last updated: 15/05/2026, 11:45:27
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x< -2**31 or x> 2**31 - 1:
            return False
        rev = 0
        org=x
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev == org

    