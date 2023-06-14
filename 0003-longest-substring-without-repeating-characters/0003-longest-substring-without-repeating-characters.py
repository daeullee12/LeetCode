class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub = deque()
        res = 0

        for c in s:
            if c in sub:
                while sub.popleft() != c:
                    continue
            sub.append(c)
            res = max(res, len(sub))
        return res

