# Last updated: 25/05/2026, 23:21:03
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        sum = 0 
4        for i in range(len(nums)):
5            sum= nums[i]+sum 
6            nums[i]=sum
7        return nums
8        