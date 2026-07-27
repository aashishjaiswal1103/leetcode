# Last updated: 27/07/2026, 17:52:47
# using the dictionary to map the index and the find the complement so that the search no increase the time complexity.
1class Solution:
2    def twoSum(self, nums: List[int], tar: int) -> List[int]:
3        out = []
4        dic = {}
5
6        for i in range(len(nums)):
7            dic[nums[i]] = i
8
9        for j in range(len(nums)):
10            com = tar - nums[j]
11            if com in dic:
12                return [j + 1, dic[com] + 1]
13    
14