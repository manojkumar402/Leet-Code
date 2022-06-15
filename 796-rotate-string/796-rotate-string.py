class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            s += s[0]
            s = s[1:]
            if s == goal:
                return True
            
        return False
            