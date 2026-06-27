# Last updated: 27/06/2026, 10:09:32
# brute force approach
1class Solution:
2    def decrypt(self, code: List[int], k: int) -> List[int]:
3        out = []
4
5        n=len(code)
6        if k == 0 :
7            out.extend([0]*n)
8            return out 
9        for i in range(n):
10            s=0
11            p=k
12            while p!=0:
13                s+=code[(i+p)%n]
14                if k>0:
15                    p-=1
16                elif k<0:
17                    p+=1
18                
19            out.append(s)
20        return out