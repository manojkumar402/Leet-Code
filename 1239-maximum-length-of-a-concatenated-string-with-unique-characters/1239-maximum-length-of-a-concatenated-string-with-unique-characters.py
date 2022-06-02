class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        arr = self.subsequence("", arr, [])
        m = 0
        for each in arr:
            m = max(m, len(each))
        return m
    def subsequence(self, p, arr, ans):
        if len(arr) == 0:
            if self.check(p):
                ans.append(p)
            return ans
        
        self.subsequence(p + arr[0], arr[1:], ans)
        self.subsequence(p, arr[1:], ans)
        return ans
    def check(self, p) -> bool:
        s = set(p)
        if len(s) - len(p) == 0:
            return True
        return False