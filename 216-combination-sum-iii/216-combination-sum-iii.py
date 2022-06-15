from copy import deepcopy
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return (self.help(1, [], [], k, 0, n))
        
    def help(self, i, tmp, ans, k, s, n):
        
        if k < 0:
            return 
        
        if s == n:
            if k == 0:
                ans.append(deepcopy(tmp))
            return
        if i == 10:
            return
        
        # Pick it
        tmp.append(i)
        s += i
        self.help(i+1, tmp, ans, k-1, s, n)
        tmp.pop()
        s -= i
        # Leave it
        self.help(i+1, tmp, ans,k,s,n)
        
       
        return ans