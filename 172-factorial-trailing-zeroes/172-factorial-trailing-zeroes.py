class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        ans = self.fact(n)
        c = 0 
        for i in reversed(str(ans)):
            if int(i) == 0:
                c += 1
            else:
                break
        return c
        
        
    def fact(self, n)->int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return n * self.fact(n-1)

            