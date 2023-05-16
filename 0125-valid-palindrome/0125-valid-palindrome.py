class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #solution 1: built-in function, extra memory
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()

        # return newStr == newStr[::-1]

        #solution 2: pointer, no extra memory -> O(n), O(1)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while l < r and not self.alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1

        return True


    def alnum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))



