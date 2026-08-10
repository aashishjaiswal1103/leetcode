# Last updated: 10/08/2026, 18:57:13
1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        stack = []
4        d = {}
5
6        for ch in s:
7            if ch not in d:
8                d[ch] = 1
9            else:
10                d[ch] += 1
11
12        for ch in s:
13
14            d[ch] -= 1
15
16            if ch in stack:
17                continue
18
19            while stack and d[stack[-1]] > 0 and stack[-1] > ch:
20                stack.pop()
21
22            stack.append(ch)
23
24        return "".join(stack)