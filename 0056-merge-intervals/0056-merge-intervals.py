class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        intervals.sort(key = lambda i : i[0]) # sorted by start value, TC O(nlogn)
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                if res[-1][1] < intervals[i][0]: 
                    res.append(intervals[i])                   
                else:
                    res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]

    
        return res
