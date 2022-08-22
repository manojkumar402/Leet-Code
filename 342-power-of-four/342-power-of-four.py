class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.powFour(n)
        
    def powFour(self,n)->bool:
        if n < 1:
            return False
        if n == 1:
            return True
        
        return self.powFour(n/4)
        