# Last updated: 08/08/2026, 22:54:35
# optimized version
1class Solution:
2    def asteroidCollision(self, ast: List[int]) -> List[int]:
3        stack = []
4        for k in ast :
5            while stack and stack[-1]>0 and k <0:
6                p = stack[-1]
7
8                if abs(p) > abs(k):
9                    break
10
11                elif abs(p) < abs(k):
12                    stack.pop()
13                    continue
14                else:
15                    stack.pop()
16                    break
17            else : 
18                stack.append(k)
19        return stack