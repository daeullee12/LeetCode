class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        output = str()

        p = 0
        while p < len(word1) and p < len(word2):
            output += word1[p] + word2[p]
            p += 1

        return output + word1[p:] + word2[p:]
        