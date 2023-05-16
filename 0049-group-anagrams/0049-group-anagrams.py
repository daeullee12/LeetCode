class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #solution 1: sorted() function, -> O(m*nlogn)
        # hmap = {}

        # for word in strs:
        #     s_word = str(sorted(word))
        #     if s_word in hmap.keys():
        #         hmap[s_word].append(word)
        #     else:
        #         hmap[s_word] = [word]

        # return hmap.values()

        #solution 2: 

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
          
            res[tuple(count)].append(word)
        
        return res.values()
            


