class Solution:
    def reverseVowels(self, s: str) -> str:
        st = []
        v = []
        vow = {'a', 'e', 'i','o','u','A','E','I','O','U'}
        for ch in s:
            if ch in vow:
                v.append(ch)
                st.append(None)
            else:
                st.append(ch)
        for i in range(len(st)-1,-1,-1):
            if st[i] == None:
                st[i] = v.pop(0)
        return "".join(st)
        