class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c = 0
        while start > 0 and goal > 0:
            if start & 1 != goal & 1:
                c += 1
            start = start >> 1
            goal = goal >> 1
        while start > 0:
            if start & 1:
                c += 1
            start = start >> 1
        # print(goal)
        while goal > 0:
            if goal & 1:
                c += 1
            goal = goal >> 1
        return c