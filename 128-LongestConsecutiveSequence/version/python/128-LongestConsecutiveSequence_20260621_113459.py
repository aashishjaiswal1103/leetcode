# Last updated: 21/06/2026, 11:34:59
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        ans = []
5
6        for i in range(len(nums)):
7            # Skip duplicate first numbers
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            left = i + 1
12            right = len(nums) - 1
13
14            while left < right:
15                total = nums[i] + nums[left] + nums[right]
16
17                if total < 0:
18                    left += 1
19
20                elif total > 0:
21                    right -= 1
22
23                else:
24                    ans.append([nums[i], nums[left], nums[right]])
25
26                    left += 1
27                    right -= 1
28
29                    # Skip duplicate left values
30                    while left < right and nums[left] == nums[left - 1]:
31                        left += 1
32
33                    # Skip duplicate right values
34                    while left < right and nums[right] == nums[right + 1]:
35                        right -= 1
36
37        return ans