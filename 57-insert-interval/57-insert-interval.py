class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        tmp = intervals[0]
        ans = []
        for each in intervals:
            if each[0] <= tmp[1]:
                tmp[1] = max(each[1], tmp[1])
            else:
                ans.append(tmp)
                tmp = each
        ans.append(tmp)
        return ans
             