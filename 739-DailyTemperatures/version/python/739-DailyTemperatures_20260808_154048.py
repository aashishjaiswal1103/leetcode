# Last updated: 08/08/2026, 15:40:48
# optima soltuion but storin gthe index value
1class Solution:
2    def dailyTemperatures(self, temp: List[int]) -> List[int]:
3        n= len(temp)
4        ans=[0]*n
5        stack=[]
6        dic={}
7        for i in range(n-1,-1,-1):
8            dic[temp[i]]=i
9            while stack and temp[stack[-1]]<=temp[i]:
10                stack.pop()
11            if stack:
12                ans[i]=stack[-1]-i
13            stack.append(i)
14        return ans