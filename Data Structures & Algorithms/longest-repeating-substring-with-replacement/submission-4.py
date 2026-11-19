class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        sub_hash = {}
        max_length = 0

        while j < len(s):
            sub_hash[s[j]] = sub_hash.get(s[j], 0) + 1
            max_count = max(sub_hash.values())
            num_replacements = j - i - max_count + 1

            if num_replacements > k:
                sub_hash[s[i]] -= 1
                i += 1
            
            max_length = max(max_length, j - i + 1)
            j += 1
            
        return max_length




