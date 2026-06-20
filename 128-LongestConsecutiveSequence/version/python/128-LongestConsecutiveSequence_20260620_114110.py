# Last updated: 20/06/2026, 11:41:10
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        s= set(nums)
4        mcount = 0 
5        for nums in s:
6            if nums-1 not in s:
7                count=1
8                while nums+count in s:
9                    count+=1
10                mcount = max(count , mcount)
11        return mcount 