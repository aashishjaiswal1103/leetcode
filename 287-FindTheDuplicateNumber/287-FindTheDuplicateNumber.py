# Last updated: 23/06/2026, 00:13:29
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic ={}
        for ch in nums :
            if ch not in dic:
                dic[ch]=1
            else :
                return ch 
        