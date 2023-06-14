class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub = deque()
        res = 0

        for c in s:
            print(sub)
            if c in sub:
                while True:
                    if sub.popleft() == c:
                        break
                    continue
            sub.append(c)
            res = max(res, len(sub))
        return res

