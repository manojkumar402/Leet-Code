class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for each in s:
            if each == '#' and len(stack1) > 0:
                stack1.pop()
            elif each != "#":
                stack1.append(each)
        
        for each in t:
            if each == '#' and len(stack2) > 0:
                stack2.pop()
            elif each != "#":
                stack2.append(each)
        # print(stack1)
        # print(stack2)
        if stack1 == stack2:
            return True
        else:
            return False