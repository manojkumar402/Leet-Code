class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = [i for i in range(1, n+1)]
        return (self.rec([],a,k,[]))
        
    def rec(self, p, up, k, ans):
        if len(p) == k:
            if p not in ans:
                ans.append(p)
        if len(up) == 0:
            return
        ch = up[0]
        self.rec(p, up[1:], k, ans)
        self.rec(p + [ch], up[1:], k, ans)
        
        return ans