# merge overlapping: I: [[1,3],[2,6],[8,10],[15,18]] O: [[1,6],[8,10],[15,18]] 
# I: [[1,4], [2,3]] O: [[1,4]]
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for pair in sorted(intervals, key=lambda x : x.start):
            if res and pair.start <= res[-1].end:
                res[-1].end = max(res[-1].end, pair.end)
            else:
                res.append(pair)
        return res