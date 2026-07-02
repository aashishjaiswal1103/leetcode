# Last updated: 02/07/2026, 22:48:56
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        left, right = 1, n
11
12        while left <= right:
13            mid = (left + right) // 2
14
15            g = guess(mid)
16
17            if g == 0:
18                return mid
19            elif g == 1:
20                left = mid + 1
21            else:
22                right = mid - 1