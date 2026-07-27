# Last updated: 27/07/2026, 18:14:16
# using the sliding window
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        l =0
4        r = 0  
5        count = 0 
6        mcount = 0 
7        for ch in nums:
8            if nums[r]==1:
9                count+=1
10                r+=1
11            elif nums[r]==0 :
12                mcount = max(mcount , count)
13                count = 0 
14                r+=1
15                l=r
16        mcount= max(mcount , count )
17        return mcount 
18
19        