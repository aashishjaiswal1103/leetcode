# Last updated: 18/06/2026, 11:52:39
1class Solution:
2    def twoSum(self, nums: List[int], tar: int) -> List[int]:
3        i = 0 
4        j = len(nums)- 1
5        out=[0 ,0]
6        while i <j :
7            if nums[i]+nums[j] == tar:
8                out[0]=i+1
9                out[1]=j+1
10                break
11            elif (nums[i]+nums[j])< tar :
12                i+=1
13            else :
14                j-=1
15        return out
16                