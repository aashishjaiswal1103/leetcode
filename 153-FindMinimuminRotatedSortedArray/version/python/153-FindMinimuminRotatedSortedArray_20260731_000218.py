# Last updated: 31/07/2026, 00:02:18
# dividing them into 2 zone
1class Solution:
2    def findMin(self, arr: List[int]) -> int:
3        left = 0
4        right = len(arr) - 1
5
6        while left <= right:
7            mid = left + (right - left) // 2
8            if arr[left] <= arr[mid] and arr[left] <= arr[right]:
9                right = mid - 1
10            elif arr[right] <= arr[left] and arr[right] <= arr[mid]:
11                left = mid + 1
12            elif arr[mid] <= arr[left] and arr[mid] <= arr[right]:
13                right = mid
14
15        return arr[mid]