class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        res = [0] * len(temperatures)
        stack = [] # [index, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append([i, t])
             
        return res

