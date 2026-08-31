class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_length = 0

        if len(s) == 0:
            return 0
        
        else:
            seen = set()
            while j < len(s):
                if s[j] not in seen:
                    seen.add(s[j])
                    max_length = max(max_length, len(seen))
                    j += 1
                else:
                    seen.remove(s[i])
                    i += 1

        return max_length


