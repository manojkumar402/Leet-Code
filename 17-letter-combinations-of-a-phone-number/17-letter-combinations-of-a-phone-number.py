class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {'2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}
        return self.help(0,digits, '',[],d)
        
    def help(self,i, digits, tmp, ans,d)->List[str]:
        if i == len(digits):
            ans.append(tmp)
            return
        
        st = d[digits[i]]
        for j in range(len(st)):
            tmp += st[j]
            self.help(i+1, digits, tmp, ans, d)
            tmp = tmp[:-1]
            
        return ans
        
        