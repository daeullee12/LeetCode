class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        hmap = set()
        for c in sentence:
            hmap.add(c)
        
        return len(hmap) == 26