# Last updated: 08/08/2026, 22:38:51
1class Solution:
2    def asteroidCollision(self, ast: List[int]) -> List[int]:
3        stack = []
4
5        for i in range(len(ast)):
6            k = ast[i]
7
8            if not stack or (stack[-1] * k) > 0:
9                stack.append(k)
10                continue
11            if stack[-1] < 0 and k > 0:
12                stack.append(k)
13                continue
14
15            while stack and (stack[-1] * k) < 0:
16                p = stack.pop()
17
18                if abs(p) == abs(k):
19                    k = 0
20                    continue
21
22                elif abs(p) > abs(k):
23                    stack.append(p)
24                    k = 0
25                    continue
26          
27            if k != 0:
28                stack.append(k)
29
30        return stack