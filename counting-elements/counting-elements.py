class Solution:
    def countElements(self, arr: List[int]) -> int:
        myset = set(arr)
        output = 0
        
        for n in arr:
            if n + 1 in myset:
                output += 1
        
        return output
                