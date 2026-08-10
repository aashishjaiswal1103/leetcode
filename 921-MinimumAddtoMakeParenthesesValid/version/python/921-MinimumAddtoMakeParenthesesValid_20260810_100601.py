# Last updated: 10/08/2026, 10:06:01
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        stack = []
4        for ch in s: 
5            if stack  and ((ch==")" and stack[-1]=="(") or (ch=="}" and stack[-1]=="{")  or (ch=="]" and stack[-1]=="[") ):
6                stack.pop()
7            else:
8                stack.append(ch)
9        return len(stack)