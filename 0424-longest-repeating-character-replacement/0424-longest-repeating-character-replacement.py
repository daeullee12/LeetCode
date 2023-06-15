class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        char = {}

        for r in range(len(s)):
            if s[r] not in char:
                char[s[r]] = 0
            char[s[r]] += 1

            if r - l - max(char.values()) >= k:
                char[s[l]] -= 1
                l += 1
        
        return r - l + 1






