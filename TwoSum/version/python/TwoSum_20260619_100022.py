# Last updated: 19/06/2026, 10:00:22
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        max = 0 
4        i = 0 
5        j = len(height) - 1 
6        while i < j :
7            x = min( height[i] , height[ j ])
8            area = x*(j-i)
9            if height[i]< height[j]:
10                i +=1
11            else: j -=1
12            if area >=max:
13                 max = area
14        return max
15        