import numpy as np
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        values = []
        l = len(nums)
        for i in range(l):
            k = nums[i]
            nums.remove(k)
            values.append(np.prod(nums))
            nums.insert(i,k)
        return values
    
s= Solution()
print(s.productExceptSelf([1,2,3,4]))