class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(magazine)
        c=0
        for each in ransomNote:
            if each in a:
                a.remove(each)
                c+=1
        if c == len(ransomNote):
            return True
        else:
            return False
        