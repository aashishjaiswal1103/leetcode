# Last updated: 23/06/2026, 12:04:57
'''
Approach : Use two pointers (i from left, j from right); move them inward, swapping whenever an odd number is on the left and an even number is on the right, so all evens end up before odds.
Time Complexity: O(n) — each pointer traverses the array at most once.
Space Complexity: O(1) — sorting is done in-place without using extra memory.
'''

1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        i = 0
4        j = len(nums) - 1
5
6        while i < j:
7            if nums[i] % 2 > nums[j] % 2:
8                nums[i], nums[j] = nums[j], nums[i]
9
10            if nums[i] % 2 == 0:
11                i += 1
12
13            if nums[j] % 2 == 1:
14                j -= 1
15
16        return nums