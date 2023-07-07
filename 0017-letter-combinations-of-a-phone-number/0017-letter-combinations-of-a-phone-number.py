class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        word = []

        if len(digits) == 0:
            return []
            
        def backtrack(i):
            if i == len(digits):
                res.append(''.join(word))
                return
            
            letters = self.mapping(digits[i])
            for j in range(len(letters)):
                word.append(letters[j])
                backtrack(i + 1)
                word.pop()
        
        backtrack(0)

        return res

        
    def mapping(self, digit):
        dic = {2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]}
        return dic[int(digit)]