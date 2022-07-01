class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
             
    
                