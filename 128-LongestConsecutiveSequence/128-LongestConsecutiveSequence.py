# Last updated: 22/06/2026, 20:54:15
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s= set(nums)
        mcount = 0 
        for nums in s:
            if nums-1 not in s:
                count=1
                while nums+count in s:
                    count+=1
                mcount = max(count , mcount)
        return mcount 