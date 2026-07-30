# Last updated: 30/07/2026, 12:47:30
'''
using the binary search where right is on n//2 and left on 1 and if it not perfect square the left  and right condition on while will be false so then we return the right as it is best closest solution 
time complexity is O(log x)
space complexity is 1
'''

1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x==0 or x==1 :
4            return x
5        left = 1 
6        right = x//2
7        while left <= right :
8            mid = left + (right-left)//2
9            t=mid*mid
10            if t == x:
11                return mid 
12            elif t<x:
13                left = mid+1
14            else:
15                right = mid-1
16        return right 