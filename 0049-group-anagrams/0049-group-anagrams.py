class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord('a')] += 1
            
            hmap[tuple(temp)].append(word)

        res = []
        for key in hmap:
            res.append(hmap[key])
        
        return res
        