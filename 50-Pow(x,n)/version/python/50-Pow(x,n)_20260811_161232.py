# Last updated: 11/08/2026, 16:12:32
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        x=0
4        n=len(s)-1
5        def rev(x,n):
6            if x>=n:
7                return
8            s[x], s[n]=s[n],s[x]
9            rev(x+1,n-1)
10        rev(x,n)
11
12            
13        
14
15
16    
17    