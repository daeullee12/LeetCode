class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # losing count
        zeros = set()
        ones = set()
        more = set()
        
        
        
        for w, l in matches:
            if w not in zeros and w not in ones and w not in more:
                zeros.add(w)
            if l not in zeros and l not in ones and l not in more:
                ones.add(l)           
            elif l in zeros:
                zeros.remove(l)
                ones.add(l)
            elif l in ones:
                ones.remove(l)
                more.add(l)
            
        
        return [sorted(list(zeros)), sorted(list(ones))]
                
            
            
                    
                    
                
            