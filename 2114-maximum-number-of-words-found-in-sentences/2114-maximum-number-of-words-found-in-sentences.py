class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for sentence in sentences:
            arr = sentence.split(' ')
            m = max(m, len(arr))
        return m