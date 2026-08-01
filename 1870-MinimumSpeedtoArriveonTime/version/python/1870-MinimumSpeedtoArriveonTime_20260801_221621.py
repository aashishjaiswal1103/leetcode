# Last updated: 01/08/2026, 22:16:21
1import math 
2class Solution:
3    def minSpeedOnTime(self, d: List[int], h: float) -> int:
4        n = len(d)
5        ans=-1
6        if h<n-1:
7            return -1
8        low = 1
9        high = 10**7
10        while low<=high:
11            s=low+(high-low)//2
12            c=0
13            k= False 
14            for i in range(n):
15                t=d[i]/s
16                if i!=n-1:
17                   c+= math.ceil(t)
18                else:c+=t
19            if c<=h :
20                ans = s 
21                high = s-1
22            else :
23                low = s+1
24        return ans 
25                
26
27
28        