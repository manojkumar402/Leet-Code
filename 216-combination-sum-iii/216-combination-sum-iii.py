from copy import copy
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return (self.help(1, [], [], k, 0, n))
        
    def help(self, i, tmp, ans, k, s, n):
        
       
        if s > n:
            return
        if len(tmp) > k:
            return
        
        if s == n and len(tmp) == k:
            ans.append(copy(tmp))
            return
        if i == 10:
            return
        
        
        # skip it
        self.help(i+1, tmp, ans, k, s, n)
        
        tmp.append(i)
        s += i
        
        self.help(i+1, tmp, ans,k,s,n)
        
        tmp.pop()
        s -= i
        
        return ans