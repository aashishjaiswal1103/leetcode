# Last updated: 15/05/2026, 11:45:25
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0 
        i = 0 
        j = len(height) - 1 
        while i < j :
            x = min( height[i] , height[ j ])
            area = x*(j-i)
            if height[i]< height[j]:
                i +=1
            else: j -=1
            if area >=max:
                 max = area
        return max
        