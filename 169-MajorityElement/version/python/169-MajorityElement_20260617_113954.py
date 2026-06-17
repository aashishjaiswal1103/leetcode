# Last updated: 17/06/2026, 11:39:54
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        dic={}
4        maj = 0 
5        k=0
6        for ch in nums :
7            if ch  not in dic:
8                dic[ch]= 1
9            else:dic[ch]+=1
10        for key , values in dic.items():
11            if maj < values:
12                maj=values
13                k=key
14        return k 
15
16