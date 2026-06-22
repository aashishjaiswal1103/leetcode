# Last updated: 22/06/2026, 23:41:10
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        dic ={}
4        for ch in nums :
5            if ch not in dic:
6                dic[ch]=1
7            else :
8                return ch 
9        