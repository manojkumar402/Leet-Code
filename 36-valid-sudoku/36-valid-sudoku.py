class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all the row 
        for r in range(len(board)):
            tmp = ""
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    tmp += board[r][c]
            s = set(tmp)
            # print(tmp, s)
            if len(s) != len(tmp):
                return False
        
        # check all the col
        for i in range(len(board[0])):
            tmp = ""
            for j in range(len(board)):
                if board[j][i] != '.':
                    tmp += board[j][i]
            s = set(tmp)
            # print(tmp, s)
            if len(s) != len(tmp):
                return False
                
        # check the 3x3 matrix
        sc = 0 
        sr = 0
        for k in range(9):
            tmp =""
            for i in range(sr, sr+3):
                for j in range(sc, sc+3):
                    if board[i][j] != '.':
                        tmp += board[i][j]
            s = set(tmp)
            if len(s) != len(tmp):
                return False
            sc = sc + 3
            if sc == 9:
                sr = sr + 3
                sc = 0
                    
                    
        return True