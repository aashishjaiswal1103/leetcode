# Last updated: 23/06/2026, 11:44:51
'''
Use k as the position of the next valid element and copy every element that is not val to the front of the array.

Time Complexity: O(n) — each element is visited exactly once.

Space Complexity: O(1) — no extra array is used; modification is done in-place.
'''

1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0 
4        n = len(nums)
5        for i in range (n):
6            if (nums[ i ]!= val ):
7                nums[k] = nums[i]
8                k+=1
9        return k    