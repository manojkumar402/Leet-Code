class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # c = 0
        i = 0
        j = 0
        print(len(t))
        if len(s) == 0:
            return True
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
                # print(i, j)
            j += 1
        
        if len(s) == i:
            return True
        return False
        
                    
      