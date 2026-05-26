# Last updated: 26/05/2026, 12:08:35
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        mul = 1
4        k = []
5        for i in range(len(nums)):
6            if nums[i] != 0:
7                mul *= nums[i]
8            else:
9                k.append(i)
10
11        for j in range(len(nums)):
12
13            if len(k) == 0:
14                nums[j] = mul // nums[j]
15            elif len(k) == 1:
16                if j == k[0]:
17                    nums[j] = mul
18                else:
19                    nums[j] = 0
20            else:
21                nums[j] = 0
22
23        return nums