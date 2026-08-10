# Last updated: 10/08/2026, 10:01:19
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        for ch in s: 
5            if stack  and ((ch==")" and stack[-1]=="(") or (ch=="}" and stack[-1]=="{")  or (ch=="]" and stack[-1]=="[") ):
6                stack.pop()
7            else:
8                stack.append(ch)
9        return True if len(stack)==0 else False
10
11