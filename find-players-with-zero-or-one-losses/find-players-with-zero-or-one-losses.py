class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_loss = set()
        
        for w, l in matches:
            if w not in one_loss and w not in more_loss:
                zero_loss.add(w)
            
            if l in zero_loss:
                zero_loss.remove(l)
                one_loss.add(l)
            elif l in one_loss:
                one_loss.remove(l)
                more_loss.add(l)
            elif l in more_loss:
                continue
            else:
                one_loss.add(l)
            
        return [sorted(list(zero_loss)), sorted(list(one_loss))]