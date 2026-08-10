# Last updated: 10/08/2026, 09:39:45
1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        stacks = []
4        stackt = []
5
6        for ch in s:
7            if ch != "#":
8                stacks.append(ch)
9            elif stacks:
10                stacks.pop()
11
12        for ch in t:
13            if ch != "#":
14                stackt.append(ch)
15            elif stackt:
16                stackt.pop()
17
18        return stacks == stackt