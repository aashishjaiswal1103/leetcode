# Last updated: 10/08/2026, 20:12:05
# not satify with this soltuion
1class Solution:
2    def minRemoveToMakeValid(self, s: str) -> str:
3        count =0 
4        stack=[]
5        for ch in s:
6            if ch=="(":
7                stack.append(ch)
8                count+=1
9            elif ch==")" :
10                if count>0:
11                    stack.append(ch)
12                    count-=1
13                else:
14                    continue
15            else:
16                stack.append(ch)
17        if count>0:
18            st =[]
19            while count>0:
20                if stack[-1]!="(":
21                    k=stack.pop()
22                    st.append(k)   
23                elif stack[-1]=="(" :
24                    k=stack.pop()
25                    count-=1
26            while st:
27                p=st.pop()
28                stack.append(p)
29
30            
31        return "".join(stack)
32    