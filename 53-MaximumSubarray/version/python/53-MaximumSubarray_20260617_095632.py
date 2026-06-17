# Last updated: 17/06/2026, 09:56:32
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        maxsum= nums[0]
4        su=0
5        for ch in nums:
6            su +=ch
7            maxsum=max(su, maxsum)
8            if su<0:
9                su=0
10        return maxsum