class Solution:
    def reverseWords(self, s: str) -> str:
        ans=''
        a = s.split(' ')
        for i in reversed(a):
            if i != '':
                ans += i+' '
        return ans[:-1]