class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        answer = 0
        
        for c in text:
            if c in set(list("balloon")):
                count[c] = 1 + count.get(c, 0)
            else:
                continue
        
        for k, v in count.items():
            if k == "l" or k == "o":
                count[k] //= 2
        
        return min(count.values()) if len(count) == 5 else 0
            
                
                
                
                