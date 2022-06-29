class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        else:
            a = self.rec([1], [], numRows, 1)
            a.insert(0, [1])
            return a
    
    def rec(self, old, ans, n, i):
        if i == n:
            return ans
        tmp = [1 for i in range(len(old)+1)]
        for j in range(1, len(tmp)-1):
            tmp[j] = old[j-1] + old[j]
        ans.append(tmp)
        return self.rec(tmp, ans, n, i+1)
            