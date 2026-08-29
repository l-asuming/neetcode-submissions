class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        set_nums = set(nums)
        count_dict = {num: nums.count(num) for num in set_nums}
        count_dict = {num: count for num, count in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}

        return list(count_dict.keys())[:k]