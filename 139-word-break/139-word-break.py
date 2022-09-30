class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        self.dp = [[[-1 for k in range(2)] for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        return self.help(0, 0, s, wordDict, 0)
        
        
    def help(self, st, ed, s, words, flag):
        if ed > len(s):
            return False
        if ed == len(s) and flag:
            return True
        if ed == len(s) and not flag:
            return False
        
        if self.dp[st][ed][flag] != -1:
            return self.dp[st][ed][flag]
        l,r = None, None
        if s[st:ed+1] in words:
            l = self.help(ed+1, ed+1, s, words, 1)
            # lowda = self.help(st, ed+1, s, words, False)
        r = self.help(st, ed+1, s, words, 0)
        self.dp[st][ed][flag] = l or r
        return self.dp[st][ed][flag]
  # Points to note  
# for every word in wordDict we have len(wordDict) - 1 optins to choose so make those recursion calls based and check for base conditions.
