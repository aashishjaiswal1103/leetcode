# Last updated: 18/06/2026, 11:33:49
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False
5        dic1 ={}
6        for ch in s :
7            if ch not in dic1 :
8                dic1[ch] = 1
9            else :
10                dic1[ch] +=1
11        for ch in t :
12            if ch in dic1 :
13                dic1[ch] -= 1 
14            else :return False 
15        if all(value == 0 for value in dic1.values()):
16            return True
17        else :return False