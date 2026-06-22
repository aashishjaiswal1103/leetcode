# Last updated: 22/06/2026, 20:54:10
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        maj = 0 
        k=0
        for ch in nums :
            if ch  not in dic:
                dic[ch]= 1
            else:dic[ch]+=1
        for key , values in dic.items():
            if maj < values:
                maj=values
                k=key
        return k 

