# Last updated: 19/06/2026, 09:39:44
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dic = {}
4        
5        for i in range(len(nums)):
6            complement = target - nums[i]
7            
8            if complement in dic:
9                return [dic[complement], i]
10            
11            dic[nums[i]] = i
12        
13        return []