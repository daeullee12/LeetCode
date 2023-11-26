class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        seen = set()
        
        for c in sentence:
            if c not in seen:
                seen.add(c)
        
        if len(seen) == 26:
            return True
        else: return False