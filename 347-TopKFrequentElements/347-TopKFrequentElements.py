# Last updated: 22/06/2026, 20:53:52
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for ch in nums:
            dic[ch] = dic.get(ch , 0 )+1 
        freq= sorted(dic , key=dic.get , reverse = True )
        return freq[:k]