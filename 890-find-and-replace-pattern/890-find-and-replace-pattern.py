class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # print(self.check("ccc", "abb"))
        ans = []
        for word in words:
            if self.check(word, pattern):
                ans.append(word)
        return ans
                    
                    
    def check(self, word, pattern):
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = word[i]
            else:
                if d[pattern[i]] != word[i]:
                    # print(d, word[i])
                    return False

        if len(set(d.values())) == len(set(pattern)):
            return True
        return False