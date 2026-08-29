import numpy as np
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        values = []
        l = len(nums)
        for i in range(l):
            k = nums[i]
            nums.remove(k)
            values.append(np.cumprod(nums)[l-2])
            nums.insert(i,k)
        return values