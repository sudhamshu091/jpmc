class Solution:
    def getMergedIntervals(self, intervals):
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda i: i[0])

        output = []

        start, end = intervals[0]

        for i in range(1, len(intervals)):
            star, en = intervals[i]

            if star <= end:

                end = max(end, en)
            else:
                output.append([start, end])
                start, end = star, en

        output.append([start, end])
        return output
        
s = Solution()
print(s.getMergedIntervals([[7,7],[2,3],[6,11],[1,2]]))
