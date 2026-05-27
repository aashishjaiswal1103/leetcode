# Last updated: 27/05/2026, 13:33:40
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        k = []
        for i in range(len(nums)):
            if nums[i] != 0:
                mul *= nums[i]
            else:
                k.append(i)

        for j in range(len(nums)):

            if len(k) == 0:
                nums[j] = mul // nums[j]
            elif len(k) == 1:
                if j == k[0]:
                    nums[j] = mul
                else:
                    nums[j] = 0
            else:
                nums[j] = 0

        return nums