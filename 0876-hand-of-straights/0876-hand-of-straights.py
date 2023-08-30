class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        while hand:
            start = hand[0]
            for i in range(groupSize):
                if start in hand:
                    hand.remove(start)
                    start += 1
                else: return False
        
        return True