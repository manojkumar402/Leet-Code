class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        t = {}
        for word in words:
            tmp = ''
            for each in word:
                tmp += code[ord(each) - ord('a')]
            if tmp not in t:
                t[tmp] = 1
            else:
                t[tmp] += 1
                
        return len(t)
        