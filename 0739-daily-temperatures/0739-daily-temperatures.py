class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        res = [0] * len(temperatures)
        stack = [] # [index, temp]

        for i, t1 in enumerate(temperatures):
            while stack and t1 > stack[-1][1]:
                j, t2 = stack.pop()
                res[j] = i - j
            
            stack.append([i, t1])
             
        return res

