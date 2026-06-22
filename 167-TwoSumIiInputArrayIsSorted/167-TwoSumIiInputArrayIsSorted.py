# Last updated: 22/06/2026, 20:54:12
class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        i = 0 
        j = len(nums)- 1
        while i <j :
            su= nums[i]+nums[j]
            if su> tar:
                j-=1
            elif su< tar :
                i+=1
            else :
                return[i+1, j+1]