class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1=[0] * 26
        arr2=[0] * 26
        for each in s:
            idx = ord(each) - 97
            if arr1[idx] == 0:
                arr1[idx] = 1
            else:
                arr1[idx] += 1
        for each in t:
            idx = ord(each) - 97
            if arr2[idx] == 0:
                arr2[idx] = 1
            else:
                arr2[idx] += 1
        for i in range(0,len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True