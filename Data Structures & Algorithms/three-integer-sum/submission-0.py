def twoSum(numbers: list[int], target: int, start_idx: int) -> list[list[int]]:
    i = start_idx
    j = len(numbers) - 1
    valid_duos = []
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            valid_duos.append([numbers[i], numbers[j]])
            i += 1
            while i < j and numbers[i] == numbers[i-1]: i += 1
        elif s > target:
            j -= 1
        else:
            i += 1
    return valid_duos

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        valid_combos = []
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]: continue
            two_sum_results = twoSum(nums, -nums[k], k + 1)
            for duo in two_sum_results:
                valid_combos.append(duo + [nums[k]])
        return valid_combos