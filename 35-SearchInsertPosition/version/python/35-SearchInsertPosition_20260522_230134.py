# Last updated: 22/05/2026, 23:01:34
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        i = len(digits) - 1
4
5        while i >= 0:
6            if digits[i] != 9:
7                digits[i] += 1
8                return digits
9            else:
10                digits[i] = 0
11                i -= 1
12
13        digits.insert(0, 1)
14        return digits