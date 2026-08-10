# Last updated: 10/08/2026, 16:48:23
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        stack = []
4
5        for ch in num:
6            while k > 0 and stack and stack[-1] > ch:
7                stack.pop()
8                k -= 1
9
10            stack.append(ch)
11
12        if k > 0:
13            stack = stack[:-k]
14
15        result = "".join(stack).lstrip("0")
16
17        return result if result else "0"
18        