# Last updated: 20/06/2026, 10:12:36
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        dic={}
4        for ch in nums:
5            dic[ch] = dic.get(ch , 0 )+1 
6        freq= sorted(dic , key=dic.get , reverse = True )
7        return freq[:k]