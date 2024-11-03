class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        n = len(intervals)
        start, end = newInterval

        resInterval = list()

        for i, si in enumerate(intervals):
            if end < si[0]:
                resInterval = resInterval + [[start, end]] + intervals[i:]
                return resInterval
            elif si[1] < start:
                resInterval.append(si)
            elif si[0] <= start <= si[1]:
                start = si[0]
                end = max(end, si[1])
            elif si[0] <= end <= si[1]:
                start = min(start, si[0])
                end = si[1]

        resInterval.append([start, end])
        return resInterval
