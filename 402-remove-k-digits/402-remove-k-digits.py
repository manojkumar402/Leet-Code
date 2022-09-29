class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        num = "10200" k = 1
        stack = [0, 2, 0, 0]
        i = 1
        """
        
        num=list(num)
        stack,i=[num[0]],1
        
        while i<len(num):
            while stack and k>0 and num[i]<stack[-1]:
                stack.pop()
                k-=1
                
            stack.append(num[i])
            i+=1
            
        while k>0:
            stack.pop()
            k-=1
        stack="".join(stack)
        return stack.lstrip("0") if stack!="" and int(stack)!=0 else "0"
