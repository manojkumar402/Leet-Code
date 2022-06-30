class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        j = 0
        while i < len(pushed):
            s.append(pushed[i])
            while len(s) > 0 and s[-1] == popped[j]:
                s.pop()
                j+=1
            i+=1
        if len(s) != 0:
            return False
        return True
