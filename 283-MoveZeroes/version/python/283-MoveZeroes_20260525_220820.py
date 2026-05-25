# Last updated: 25/05/2026, 22:08:20
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        j = 0
4        for i in range (len(nums)):
5            if nums[i]!=0:
6                nums[j], nums[i] = nums[i] , nums[j]
7                j+=1