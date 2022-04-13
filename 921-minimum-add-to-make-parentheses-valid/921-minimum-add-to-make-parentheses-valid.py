class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 1:
            return 1
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if ('(' not in stack) or (len(stack) == 0):
                    stack.append(char)
                else:
                    stack.pop()
        return len(stack)
                    

        
        