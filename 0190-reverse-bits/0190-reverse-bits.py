class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # o = str()

        # while n:
        #     o += str(n % 2)
        #     n >>= 1
        
        # while len(o) < 32:
        #     o += str(0)

        # return(int(o, 2))

        res = 0

        for i in range(32):
            res |= ((n >> i) & 1) << (31 - i)
        
        return res