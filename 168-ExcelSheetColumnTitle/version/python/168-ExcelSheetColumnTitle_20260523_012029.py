# Last updated: 23/05/2026, 01:20:29
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        result = ""
4        n = columnNumber
5        while n>0:
6            remainder = n%26 
7            if remainder==0:
8                last = 'Z'
9                n=(n//26)-1
10            else:
11                last = chr(ord('A')+remainder-1)
12                n=n//26
13            result = last + result 
14        return result 
15        