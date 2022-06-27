class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = {}
        sdict = {}
        ans = []
        for ch in p:
            if ch in pdict:
                pdict[ch] += 1
            else:
                pdict[ch] = 1
        # print(pdict)
        i = 0
        j = 0
        while j < len(s):
            if s[j] in sdict:
                sdict[s[j]] += 1
            else:
                sdict[s[j]] = 1
            if j-i+1<len(p):
                j+=1
            elif j-i+1 == len(p):
                if sdict == pdict:
                    ans.append(i)
                if sdict[s[i]] == 1:
                    sdict.pop(s[i])
                else:
                    sdict[s[i]] -= 1
                i+=1
                j+=1
        return (ans)