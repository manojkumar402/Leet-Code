class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.powThree(n)
        
    def powThree(self,n)->bool:
        if n < 1:
            return False
        if n == 1:
            return True
        
        return self.powThree(n/3)
        
            
    
    
        