class Solution:
    def partition(self, s: str) -> List[List[str]]: 
        return self.help(s, [], [])
        
    def help(self,s, tmp, ans):
        if not s:
            ans.append(tmp)
            return
        
        for i in range(1, len(s)+1):
            sub = s[:i]
            if sub == sub[::-1]:
                self.help(s[i:], tmp + [sub], ans)
        return ans
