class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1

        while i <= j:
            
            k = (i+j)//2

            if nums[k] < target:
                i = k+1
            
            elif nums[k] > target:
                j = k-1
            
            elif nums[k] == target:
                return k
        
        return -1
        