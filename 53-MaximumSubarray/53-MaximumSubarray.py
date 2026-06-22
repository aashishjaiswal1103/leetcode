# Last updated: 22/06/2026, 20:54:20
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum= nums[0]
        su=0
        for ch in nums:
            su +=ch
            maxsum=max(su, maxsum)
            if su<0:
                su=0
        return maxsum