class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return (self.All([],nums, []))
    
    # def All(self, p,up)->list[list]:
    #     if len(up) == 0:
    #         l = []
    #         l.append(p)
    #         return l
    #     ch = up[0]
    #     ans = []
    #     for i in range(len(p) + 1):
    #         f = p[0:i]
    #         s = p[i:]
    #         ans = ans + self.All(f+[ch]+s, up[1:])
    #     return ans
    
    def All(self, p,up,ans)->list[list]:
        if len(up) == 0:
            ans.append(p)
            return 
        ch = up[0]
        for i in range(len(p) + 1):
            f = p[0:i]
            s = p[i:]
            self.All(f+[ch]+s, up[1:], ans)
        return ans