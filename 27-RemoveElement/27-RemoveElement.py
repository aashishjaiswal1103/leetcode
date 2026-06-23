# Last updated: 24/06/2026, 00:48:24
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        n = len(nums)
        for i in range (n):
            if (nums[ i ]!= val ):
                nums[k] = nums[i]
                k+=1
        return k    