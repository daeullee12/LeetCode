class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i : i[0]) # sorted by start value, TC O(nlogn)
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if lastEnd < start: 
                res.append([start, end])                   
            else:
                res[-1][1] = max(lastEnd, end)

    
        return res
