# Last updated: 10/08/2026, 09:48:39
1class Solution:
2    def makeGood(self, s: str) -> str:
3        stack = []
4
5        for ch in s:
6            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
7                stack.pop()
8            else:
9                stack.append(ch)
10
11        return "".join(stack)