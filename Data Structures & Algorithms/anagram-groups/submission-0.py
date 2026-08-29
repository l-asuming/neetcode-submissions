class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        groupAnagrams = []
        indexes = []

        sorted_strs_list = [''.join(sorted(str_)) for str_ in strs]
        sorted_strs_set = set(sorted_strs_list)

        for i in sorted_strs_set:
            indexes.append([k for k, v in enumerate(sorted_strs_list) if v == i])
        
        for i in range(len(indexes)):
            anagrams = [strs[k] for k in indexes[i]]
            groupAnagrams.append(anagrams)
        
        return groupAnagrams