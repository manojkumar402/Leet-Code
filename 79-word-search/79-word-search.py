from copy import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    # call the fn
                    if self.help(r, c, word, board, 0,visited):
                        return True
        return False

    
    # Fraz Method
    
    def help(self, r, c, word, board, i, visited):
        if i >= len(word):
            return True
        if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or board[r][c] != word[i] or visited[r][c] == 1:
            return False
        
        
        visited[r][c] = 1
        op1 = self.help(r+1, c, word, board, i+1, visited)
        op2 = self.help(r, c+1, word, board, i+1, visited)
        op3 = self.help(r-1, c, word, board, i+1, visited)
        op4 = self.help(r, c-1, word, board, i+1, visited)
        
        visited[r][c] = 0
        
        return op1 or op2 or op3 or op4
     # Kunal Method
#     def help(self, r, c, word, board, i, tmp, visited):
#         if i == len(word):
#             print(tmp)
#             return 
        
#         if word[i] != board[r][c]:
#             return 
#         if visited[r][c] == 1:
#             return 
        
        
#         visited[r][c] = 1
#         tmp.append([r,c])
#         # check left
#         if c > 0:
#             op1 = self.help(r, c-1, word, board, i+1, tmp, visited)
#         # check right
#         if c < len(board[0])-1:
#             op2 = self.help(r, c+1, word, board, i+1, tmp, visited)
#         # check down
#         if r < len(board)-1:
#             op3 = self.help(r+1, c, word, board, i+1, tmp, visited)
#         # check up
#         if r > 0:
#             op4 = self.help(r-1, c, word, board, i+1, tmp, visited)
        
#         visited[r][c] = 0
#         tmp.pop()
        

        
