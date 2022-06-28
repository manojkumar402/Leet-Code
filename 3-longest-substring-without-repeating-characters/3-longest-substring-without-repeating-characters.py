class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        d = {}
        ans = 0
        while j < len(s):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            
            if len(d) == j-i+1:
                ans = max(ans, j-i+1)
                j+=1
            elif len(d) < j-i+1:
                while len(d) < j-i+1:
                    if d[s[i]] == 1:
                        d.pop(s[i])
                    else:
                        d[s[i]] = d[s[i]] - 1
                    i += 1
                j += 1
        return ans