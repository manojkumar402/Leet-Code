class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for ch in t:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        count = len(d)
        ans = ["", 0]
        # count -> number of unique characters
        i = 0
        j = 0
        while j < len(s):
            if s[j] in d:
                d[s[j]] = d[s[j]] - 1
                if d[s[j]] == 0:
                    count = count - 1
            if count == 0:
                # ans is found 
                # move i ptr to find smaller answer
                while count == 0:
                    if s[i] in d:
                        d[s[i]] += 1
                        if d[s[i]] > 0:
                            count += 1
                    i+=1
                l = j - i + 2
                if ans[1] == 0:
                    ans[1] = l
                    ans[0] = s[i-1:j+1]
                else:
                    if l < ans[1]:
                        ans[1] = l
                        ans[0] = s[i-1:j+1] 
                j += 1
            elif count > 0:
                j += 1
        return ans[0]