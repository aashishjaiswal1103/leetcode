# Last updated: 24/06/2026, 10:47:01
'''
using prefix sum 
time(n+n)
'''

1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        rs=sum(nums)
4        ls=0
5        for i in range(len(nums)):
6            rs-=nums[i]
7            if ls==rs:
8                return i
9            ls+=nums[i]
10        return -1
11
12
13