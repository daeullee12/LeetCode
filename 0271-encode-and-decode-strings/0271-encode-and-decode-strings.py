class Codec:
    
    def encode(self, strs: List[str]) -> str:

        self.d = {}
        result = ""
        i = 0

        for s in strs:
            self.d[i] = s
            result += s
            i += 1
        
        return result

    def decode(self, s: str) -> List[str]:
        
        i = 0
        self.strs = []
        for i in range(len(self.d)):
            self.strs.append(self.d[i])
        
        return self.strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))