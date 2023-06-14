class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sub = deque()
        # res = 0

        # for c in s:
        #     if c in sub:
        #         while sub.popleft() != c:
        #             continue
        #     sub.append(c)
        #     res = max(res, len(sub))
        # return res


        l = 0
        charSet = set()
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res
                    