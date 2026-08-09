# Last updated: 09/08/2026, 23:43:58
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4
5        for k in s:
6            if k != "]":
7                stack.append(k)
8                continue
9
10            string = ""
11            while stack and stack[-1] != "[":
12                string = stack.pop() + string
13
14
15            stack.pop()
16            number = ""
17            while stack and stack[-1].isdigit():
18                number = stack.pop() + number
19
20            number = int(number)
21
22            string = string * number
23
24            stack.append(string)
25
26        return "".join(stack)