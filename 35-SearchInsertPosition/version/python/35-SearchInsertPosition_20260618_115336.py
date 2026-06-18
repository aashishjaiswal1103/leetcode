# Last updated: 18/06/2026, 11:53:36
1class Solution:
2    def twoSum(self, nums: List[int], tar: int) -> List[int]:
3        i = 0 
4        j = len(nums)- 1
5        while i <j :
6            su= nums[i]+nums[j]
7            if su> tar:
8                j-=1
9            elif su< tar :
10                i+=1
11            else :
12                return[i+1, j+1]