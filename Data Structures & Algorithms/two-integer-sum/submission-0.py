class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = 1
        k = len(nums)
        while i <= k - 2:
            if nums[i] + nums[j] == target:
                return [i,j]
            else:
                j += 1
            if j == k:
                i += 1
                j = i+1