# Last updated: 03/07/2026, 22:49:41
# using basic hash map
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        seen = {}
4
5        for i, num in enumerate(nums):
6            if num in seen and i - seen[num] <= k:
7                return True
8            seen[num] = i
9
10        return False