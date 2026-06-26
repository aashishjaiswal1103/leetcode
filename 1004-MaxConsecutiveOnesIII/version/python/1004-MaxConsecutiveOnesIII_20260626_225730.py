# Last updated: 26/06/2026, 22:57:30
'''
using the sliding window 
and linear traversal
'''

1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        left = 0
4        zeros = 0
5        ans = 0
6
7        for right in range(len(nums)):
8            if nums[right] == 0:
9                zeros += 1
10
11            while zeros > k:
12                if nums[left] == 0:
13                    zeros -= 1
14                left += 1
15
16            ans = max(ans, right - left + 1)
17
18        return ans