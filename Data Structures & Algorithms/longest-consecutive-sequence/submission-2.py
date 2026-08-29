class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        lengths = []

        nums_1 = list(set(nums))
        nums_1.sort()

        counter = 1

        if nums_1 == []:
            return 0
        
        for i in range(len(nums_1)-1):
            if nums_1[i+1] == nums_1[i]+1:
                counter += 1

            else:
                lengths.append(counter)
                counter = 1

        lengths.append(counter)
        
        return max(lengths)
