# Last updated: 20/06/2026, 00:05:22
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        low = 0 
4        mid = 0 
5        high = len(nums) - 1
6        
7        while mid <= high:
8            if nums[mid] == 0:
9                nums[low], nums[mid] = nums[mid], nums[low]
10                low += 1
11                mid += 1
12            elif nums[mid] == 1:
13                mid += 1
14            else:
15                nums[mid], nums[high] = nums[high], nums[mid]
16                high -= 1