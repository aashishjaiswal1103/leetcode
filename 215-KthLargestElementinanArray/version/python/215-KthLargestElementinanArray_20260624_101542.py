# Last updated: 24/06/2026, 10:15:42
# usign the sort
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        nums.sort(reverse=True)
4        return nums[k - 1]