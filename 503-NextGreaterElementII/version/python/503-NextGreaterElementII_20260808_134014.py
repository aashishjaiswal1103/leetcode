# Last updated: 08/08/2026, 13:40:14
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        ans= [-1]*n
5        stack = []
6        for i in range(2*n-1,-1,-1):
7            i=i%n
8            while stack and stack[-1]<=nums[i]:
9                stack.pop()
10            if stack:
11                ans[i]=stack[-1]
12            stack.append(nums[i])
13        return ans
14        