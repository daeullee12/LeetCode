class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # TC O(n*4^n), n = len(digits)
        res = []
        digitToChar = { "2" : "abc",
                        "3" : "def",
                        "4" : "ghi",
                        "5" : "jkl",
                        "6" : "mno",
                        "7" : "pqrs",
                        "8" : "tuv",
                        "9" : "wxyz"}

        def backtrack(i, curChar):
            if len(curChar) == len(digits):
                res.append(curChar)
                return
        
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curChar + c)
        
        if digits:
            backtrack(0, "")
        return res
