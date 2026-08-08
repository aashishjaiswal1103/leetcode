# Last updated: 08/08/2026, 10:38:21
'''
bruteforce method 
time complexity = n*n
'''

1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        n = len(nums1)
4        k = len(nums2)
5        ans = [-1] * n
6        n2 = {num: nums2.index(num) for num in nums2}
7
8        for p in range(n):
9            ch = nums1[p]
10
11            if ch in n2:
12                i = n2[ch]
13
14                for j in range(i + 1, k):
15                    if nums2[j] > ch:
16                        ans[p] = nums2[j]
17                        break
18
19        return ans