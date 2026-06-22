# Last updated: 22/06/2026, 23:33:42
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total = sum(nums)
4        left_sum = 0
5
6        for i in range(len(nums)):
7            right_sum = total - left_sum - nums[i]
8
9            if left_sum == right_sum:
10                return i
11
12            left_sum += nums[i]
13
14        return -1