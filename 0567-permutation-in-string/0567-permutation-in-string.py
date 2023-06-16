class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
         if len(s1) ==n, len(s2) == m

        """
        if len(s1) > len(s2):
            return False

        hmap1 = {}

        for c in s1:
            hmap1[c] = 1 + hmap1.get(c, 0)
        
        l = 0
        hmap2 = {}
        match = 0

        for r in range(len(s2)):
            hmap2[s2[r]] = 1 + hmap2.get(s2[r], 0)
            
            if hmap1.get(s2[r], 0) == hmap2[s2[r]]:
                match += 1

            if r - l + 1 > len(s1):
                if hmap1.get(s2[l],0) == hmap2[s2[l]]:
                    match -= 1
                hmap2[s2[l]] -= 1
                l += 1

            if match == len(hmap1):
                return True
            print(s2[r], match)

        return False
            
            
                
            




