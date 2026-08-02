# Last updated: 02/08/2026, 23:47:24
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5
6        while left < right:
7            mid = left + (right - left) // 2
8            if nums[mid] > nums[mid + 1]:
9                right = mid
10            else:
11                left = mid + 1
12        return left