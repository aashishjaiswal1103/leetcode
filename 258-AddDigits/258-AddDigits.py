# Last updated: 15/05/2026, 11:45:15
class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            total = 0

            while num > 0:
                rem = num % 10
                total += rem
                num = num // 10

            num = total

        return num