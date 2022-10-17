class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in range(0, len(haystack) - len(needle)):
        #     print(i)
        if needle in haystack:
            return haystack.index(needle)
        return -1