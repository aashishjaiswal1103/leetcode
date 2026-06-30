# Last updated: 30/06/2026, 10:08:58
# usgng the basic bakward traverse
1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        length = max(len(num1), len(num2))
4        num1 = num1.zfill(length)
5        num2 = num2.zfill(length)
6        carry=0
7        out = ""
8
9        for i in range(length-1,-1,-1):
10            su = 0 
11            su = int(num1[i])+int(num2[i])+carry
12            carry= su//10
13            digit = su%10
14            out = str(digit)+out
15        if carry:
16            out = str(carry)+out
17        return out 
18
19