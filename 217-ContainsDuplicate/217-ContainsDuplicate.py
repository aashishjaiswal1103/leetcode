# Last updated: 22/06/2026, 20:54:04
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        if len(a)!=len(nums):
            return True
        else:
            return False
    