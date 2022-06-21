class Solution:
    def removeDuplicates(self, s: str) -> str:
        # when popped from stack dont add it to stack
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif len(stack) > 0 and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        res = ""
        for each in stack:
            res += each
        return res