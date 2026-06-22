# Last updated: 22/06/2026, 20:54:30
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in dic:
                return [dic[complement], i]
            
            dic[nums[i]] = i
        
        return []