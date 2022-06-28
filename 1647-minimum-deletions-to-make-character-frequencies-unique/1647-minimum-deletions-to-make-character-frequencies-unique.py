class Solution:
    def minDeletions(self, s: str) -> int:
        d = dict()
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        freq = list(d.values())
        c = 0
        # we are using set to store the frequencies that have already seen
        
        freq_set = set()
        for i in range(len(freq)):
            while freq[i] and freq[i] in freq_set:
                freq[i] -= 1
                c +=1
            freq_set.add(freq[i])
                
        return c
                