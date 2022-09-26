class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        new = []
        for key in d:
            new.append([d[key], key])
        new.sort(reverse = True)
        res = ''
        for each in new:
            res = res + each[0] * each[1]
        return res