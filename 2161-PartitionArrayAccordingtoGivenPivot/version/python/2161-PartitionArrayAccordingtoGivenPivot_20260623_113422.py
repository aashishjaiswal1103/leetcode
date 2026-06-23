# Last updated: 23/06/2026, 11:34:22
'''
usign the 3 list to maintain order 
time = O(n) 
space=O(n)
'''

1class Solution:
2    def pivotArray(self, nums: List[int], k: int) -> List[int]:
3        s = []
4        m=[]
5        l=[]
6        for ch in nums:
7            if ch <k:
8                s.append(ch)
9            elif ch==k:
10                m.append(ch)
11            else:
12                l.append(ch)
13        return s+m+l
14        